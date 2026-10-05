"""Shared strict parsing, atomic writes, and scoped wiki validation."""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


class ContractError(ValueError):
    pass


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ContractError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def atomic_write(path, data):
    path = Path(path)
    encoded = data.encode("utf-8") if isinstance(data, str) else data
    if path.exists() and path.read_bytes() == encoded:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".write-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(encoded)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_json(path, value):
    atomic_write(path, json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def load_manifest(workspace):
    try:
        manifest = json.loads((Path(workspace) / "manifest.json").read_text(encoding="utf-8"))
        if manifest["schema_version"] != 1:
            raise ContractError("unsupported manifest version")
        if not isinstance(manifest["sources"], dict) or not isinstance(manifest["identities"], dict) or type(manifest["threshold"]) is not int or manifest["threshold"] < 2:
            raise ContractError("invalid manifest source registry/threshold")
        for sid, record in manifest["sources"].items():
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", sid) or record["source_id"] != sid or record["page"] != f"wiki/sources/{sid}.md":
                raise ContractError("invalid manifest source identity/page")
            paths = [record["raw_file"]] + [item["path"] for item in record.get("assets", [])]
            if any(not isinstance(x, str) or not x.startswith(f"raw/{sid}/") or ".." in Path(x).parts for x in paths):
                raise ContractError("unsafe manifest evidence path")
            if not re.fullmatch(r"[a-f0-9]{64}", record["sha256"]) or type(record["total_lines"]) is not int or record["total_lines"] < 0:
                raise ContractError("invalid manifest content hash/line count")
        return manifest
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise ContractError(f"invalid manifest: {exc}") from exc


def read_page(path):
    try:
        text = Path(path).read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or lines[0] != "---":
            raise ContractError("missing YAML frontmatter")
        end = next((i for i in range(1, len(lines)) if lines[i] == "---"), None)
        if end is None:
            raise ContractError("unclosed YAML frontmatter")
        fm = yaml.load("\n".join(lines[1:end]), Loader=UniqueLoader)
        if not isinstance(fm, dict):
            raise ContractError("frontmatter must be a mapping")
        return fm, "\n".join(lines[end + 1:])
    except (OSError, UnicodeError, yaml.YAMLError, TypeError) as exc:
        raise ContractError(str(exc)) from exc


def content_pages(bundle):
    return sorted(p for p in Path(bundle).rglob("*.md") if p.name not in {"index.md", "log.md"})


def without_code(text, strip_inline=True):
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            token = match[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(re.sub(r"`+[^`]*`+", "", line) if strip_inline else line)
    return "\n".join(lines)


def destinations(body):
    text = without_code(body)
    inline = re.findall(r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", text)
    definitions = dict(re.findall(r"^\[([^\]^][^\]]*)\]:\s*(<[^>]+>|\S+)", text, re.M))
    inline.extend(definitions.values())
    missing = []
    for label, ref in re.findall(r"!?\[([^\]\n]+)\]\[([^\]\n]*)\]", text):
        if label.startswith("^") or ref.startswith("^"):
            continue  # Adjacent claim footnotes are not Markdown reference links.
        key = ref or label
        if key not in definitions:
            missing.append(key)
    return [x.strip("<>") for x in inline], missing


def resolve_resource(page, resource, bundle):
    parsed = urlsplit(resource)
    if parsed.scheme or parsed.netloc:
        return None, parsed.fragment
    decoded = unquote(parsed.path)
    target = (Path(bundle) / decoded.lstrip("/")) if decoded.startswith("/") else (Path(page).parent / decoded)
    return target.resolve(), unquote(parsed.fragment)


def anchors(path):
    found, counts = set(), {}
    for line in without_code(Path(path).read_text(encoding="utf-8"), strip_inline=False).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            key = re.sub(r"[^\w\- ]", "", match[1].lower()).replace(" ", "-")
            count = counts.get(key, 0)
            counts[key] = count + 1
            found.add(key if not count else f"{key}-{count}")
    return found


def iso_time(value):
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed.utcoffset() is not None
    except ValueError:
        return False


def candidate_refs(fm):
    result = {}
    for kind in ("entities", "concepts"):
        refs = fm.get(kind, [])
        if not isinstance(refs, list) or any(not isinstance(x, str) or not re.fullmatch(rf"{kind}/[a-z0-9][a-z0-9-]*\.md", x) for x in refs):
            raise ContractError(f"{kind} must be canonical bundle-relative paths")
        result[kind] = sorted(set(refs))
    return result


def source_errors(page, fm, workspace, manifest):
    errors = []
    if fm.get("type") != "source":
        errors.append("accepted source page must have type: source")
    sid = fm.get("source_id")
    if not isinstance(sid, str):
        return ["source_id must be a string"]
    record = manifest["sources"].get(sid)
    if not record:
        return ["unknown source_id"]
    if page.relative_to(workspace).as_posix() != record["page"]:
        errors.append("source page path does not match manifest")
    raw = workspace / record["raw_file"]
    if fm.get("raw_file") != record["raw_file"] or fm.get("content_sha256") != record["sha256"]:
        errors.append("raw_file/content_sha256 do not match manifest")
    if not raw.is_file() or digest(raw.read_bytes()) != record["sha256"]:
        errors.append("immutable raw snapshot missing or changed")
    for asset in record.get("assets", []):
        path = workspace / asset["path"]
        if not path.is_file() or digest(path.read_bytes()) != asset["sha256"]:
            errors.append(f"attachment missing or changed: {asset['path']}")
    coverage = fm.get("coverage", {})
    total = record["total_lines"]
    if not isinstance(coverage, dict) or coverage.get("complete") is not True or coverage.get("total_lines") != total:
        errors.append("coverage must declare complete and exact total_lines")
    else:
        ranges = coverage.get("ranges", [])
        cursor = 1
        if not isinstance(ranges, list):
            errors.append("coverage ranges must be a list")
        else:
            for interval in ranges:
                if not isinstance(interval, list) or len(interval) != 2 or any(type(n) is not int for n in interval) or interval[0] != cursor or interval[1] < cursor:
                    errors.append("coverage ranges must be contiguous nonoverlapping line pairs")
                    break
                cursor = interval[1] + 1
            if cursor != total + 1:
                errors.append("coverage ranges do not cover every line")
    if record.get("warnings"):
        # Discovery warnings are visible in receipts, not invented evidence.
        if not fm.get("limitations"):
            errors.append("source limitations must disclose discovery warnings")
    try:
        candidate_refs(fm)
    except ContractError as exc:
        errors.append(str(exc))
    provenance = fm.get("sources", [])
    if not isinstance(provenance, list) or not any(isinstance(x, dict) and x.get("id") == sid for x in provenance):
        errors.append("source provenance must contain its source_id")
    else:
        for item in provenance:
            if isinstance(item, dict) and item.get("id") == sid and isinstance(item.get("resource"), str):
                target, _ = resolve_resource(page, item["resource"], workspace / "wiki")
                if target != raw.resolve():
                    errors.append("source provenance must point to its raw snapshot")
    return errors


def validate(workspace, scope="workspace", check_indexes=True, only=None):
    workspace = Path(workspace).resolve()
    bundle = workspace / "wiki" if (workspace / "wiki").is_dir() else workspace
    structural, evidence, warnings = [], [], []
    if not bundle.is_dir():
        return {"structural_errors": ["bundle directory does not exist"], "evidence_errors": [], "warnings": [], "valid": False}
    manifest = None
    if scope == "workspace":
        try:
            manifest = load_manifest(workspace)
        except ContractError as exc:
            evidence.append(str(exc))
    paths = [Path(only).resolve()] if only else content_pages(bundle)
    metadata = {}
    for page in paths:
        name = page.relative_to(bundle).as_posix()
        try:
            fm, body = read_page(page)
        except ContractError as exc:
            structural.append(f"{name}: {exc}")
            continue
        metadata[name] = fm
        if not isinstance(fm.get("type"), str) or not fm["type"].strip():
            structural.append(f"{name}: nonempty string type required")
        if scope == "bundle":
            continue
        for key in ("title", "description", "created"):
            if not fm.get(key):
                evidence.append(f"{name}: template requires {key}")
        if not iso_time(fm.get("created", "")):
            evidence.append(f"{name}: created needs a timezone-aware datetime")
        generated = fm.get("generated")
        if not isinstance(generated, dict) or not generated.get("by") or not iso_time(generated.get("at", "")):
            evidence.append(f"{name}: generated needs by and timezone-aware at")
        if fm.get("type") == "source" and manifest:
            evidence.extend(f"{name}: {x}" for x in source_errors(page, fm, workspace, manifest))
        text = without_code(body)
        definitions = set(re.findall(r"^\[\^([\w-]+)\]:", text, re.M))
        used = set(re.findall(r"(?<!^)\[\^([\w-]+)\](?!:)", text, re.M))
        sources = fm.get("sources", [])
        ids = set()
        if not isinstance(sources, list):
            evidence.append(f"{name}: sources must be a list of mappings")
            sources = []
        for item in sources:
            if not isinstance(item, dict) or not isinstance(item.get("resource"), str) or not isinstance(item.get("id"), str) or not re.fullmatch(r"[\w-]+", item["id"]):
                evidence.append(f"{name}: sources entries need id and resource")
                continue
            if item["id"] in ids:
                evidence.append(f"{name}: duplicate provenance id {item['id']}")
            ids.add(item["id"])
        if used - ids or used - definitions:
            evidence.append(f"{name}: footnotes lack provenance or definitions: {sorted((used-ids)|(used-definitions))}")
        if fm.get("type") in {"source", "concept", "entity"} and not used:
            evidence.append(f"{name}: at least one claim attribution required")
        refs = set()
        try:
            refs = {x for items in candidate_refs(fm).values() for x in items}
        except ContractError as exc:
            evidence.append(f"{name}: {exc}")
        targets, missing_refs = destinations(body)
        if missing_refs:
            evidence.append(f"{name}: undefined reference links: {missing_refs}")
        targets += [x["resource"] for x in sources if isinstance(x, dict) and isinstance(x.get("resource"), str)]
        targets += ["/" + x for x in refs]
        for link in targets:
            try:
                target, fragment = resolve_resource(page, link, bundle)
            except ValueError:
                evidence.append(f"{name}: invalid resource {link}")
                continue
            if target is None:
                continue
            if not check_indexes and target.is_relative_to(bundle) and target.name == "index.md":
                continue  # Navigation will be generated after content validation.
            if not target.is_relative_to(workspace):
                evidence.append(f"{name}: local link leaves workspace: {link}")
            elif not target.exists():
                candidate = target.is_relative_to(bundle) and target.relative_to(bundle).as_posix() in refs
                (warnings if candidate else evidence).append(f"{name}: {'candidate' if candidate else 'missing evidence'} {link}")
            elif fragment and target.suffix == ".md" and fragment not in anchors(target):
                evidence.append(f"{name}: missing heading #{fragment} in {link}")
        if fm.get("status") == "draft":
            warnings.append(f"{name}: draft")
    if manifest and not only:
        for sid, record in manifest["sources"].items():
            if record["page"].removeprefix("wiki/") not in metadata:
                evidence.append(f"{sid}: source page missing or unreadable")
        try:
            counts = collect_mentions(workspace)
            for kind, page_type in (("entities", "entity"), ("concepts", "concept")):
                for ref, record in counts[kind].items():
                    if record["count"] >= manifest["threshold"] and ref not in metadata:
                        evidence.append(f"{ref}: qualifying page missing")
                for name, fm in metadata.items():
                    if fm.get("type") != page_type:
                        continue
                    record = counts[kind].get(name, {"count": 0, "source_ids": []})
                    listed = fm.get("sources", [])
                    actual = {x.get("id") for x in listed if isinstance(x, dict) and isinstance(x.get("id"), str)} if isinstance(listed, list) else set()
                    if record["count"] < manifest["threshold"] or fm.get("source_count") != record["count"] or actual != set(record["source_ids"]):
                        evidence.append(f"{name}: synthesis evidence set/count does not match qualifying sources")
                    if isinstance(listed, list):
                        for item in listed:
                            if not isinstance(item, dict) or not isinstance(item.get("resource"), str) or item.get("id") not in record["source_ids"]:
                                continue
                            target, _ = resolve_resource(bundle / name, item["resource"], bundle)
                            expected = workspace / manifest["sources"][item["id"]]["page"]
                            if target != expected.resolve():
                                evidence.append(f"{name}: provenance ID points to the wrong source page: {item['id']}")
        except ContractError as exc:
            evidence.append(str(exc))
    if check_indexes and not only:
        for reserved in sorted(bundle.rglob("*.md")):
            if reserved.name == "index.md":
                text = reserved.read_text(encoding="utf-8")
                if text.startswith("---"):
                    try:
                        fm, _ = read_page(reserved)
                        if reserved != bundle / "index.md" or set(fm) != {"okf_version"} or str(fm["okf_version"]) != "0.2":
                            structural.append(f"{reserved.name}: only bundle root okf_version frontmatter allowed by this template")
                    except ContractError as exc:
                        structural.append(f"{reserved}: {exc}")
                if scope == "workspace":
                    for link in destinations(text)[0]:
                        target, _ = resolve_resource(reserved, link, bundle)
                        if target and (not target.is_relative_to(workspace) or not target.exists()):
                            evidence.append(f"{reserved.relative_to(bundle)}: invalid navigation {link}")
            elif reserved.name == "log.md":
                text = reserved.read_text(encoding="utf-8")
                headings = re.findall(r"^## (.+)$", text, re.M)
                valid_dates = []
                for heading in headings:
                    try:
                        date.fromisoformat(heading)
                        valid_dates.append(heading)
                    except ValueError:
                        structural.append(f"{reserved}: log heading must be YYYY-MM-DD: {heading}")
                if valid_dates != sorted(valid_dates, reverse=True):
                    structural.append(f"{reserved}: log must be newest first")
                if text.startswith("---"):
                    structural.append(f"{reserved}: log cannot have frontmatter")
    return {"structural_errors": structural, "evidence_errors": evidence, "warnings": sorted(set(warnings)), "valid": not structural and not evidence}


def collect_mentions(workspace):
    workspace = Path(workspace).resolve()
    manifest = load_manifest(workspace)
    result = {"entities": {}, "concepts": {}}
    for sid, record in sorted(manifest["sources"].items()):
        page = workspace / record["page"]
        fm, _ = read_page(page)
        errors = source_errors(page, fm, workspace, manifest)
        if errors:
            raise ContractError(f"{record['page']}: {'; '.join(errors)}")
        for kind, refs in candidate_refs(fm).items():
            for ref in refs:
                value = result[kind].setdefault(ref, {"source_ids": [], "source_pages": []})
                value["source_ids"].append(sid)
                value["source_pages"].append(record["page"])
    for records in result.values():
        for value in records.values():
            value["count"] = len(value["source_ids"])
            value["qualifies"] = value["count"] >= manifest["threshold"]
    return result
