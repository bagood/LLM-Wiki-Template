# ADR 0003: Generic OKF and optional producer profile

Status: proposed for owner review; parser implementation is P1.

`okf_bundle` accepts UTF-8 Markdown with safe YAML and a nonempty `type` on content
pages. Reserved indexes/logs have their format-specific treatment. A type-only
document is valid; unknown type values remain generic retrievable nodes and
unknown metadata is preserved. Broken links are warnings. No manifest, raw store,
stock fields, titles, or two-source threshold are universal requirements.

`template_workspace` adds manifest/raw hash checks, completed-source identity,
coverage/citations, declared candidates, topic engagements, two-source synthesis,
and stock `report_context` preservation. These checks supplement base conformance.
Distinct artifacts/aliases/syntheses do not establish independent corroboration.

Parse Markdown tokens rather than regex-only links. Reject duplicate YAML keys
and unsafe constructors; execute nothing. Normalize paths before containment and
symlink checks; allow companion raw paths only inside configured evidence roots.
Keep external provenance URIs without fetching. Generic provenance identity is
`(wiki_id, snapshot_id, declaring page, provenance id)` unless an explicit verified
identity mapping unifies declarations. Reused `reference-1` in the generic fixture
deliberately represents different resources.

Format authority is the pinned [OKF v0.2 revision](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/0b87c52c6ef999286c745e19998fdfcd03d5dbee/SPEC.md),
with fingerprint in the repository's `okf-spec.json`. Producer conventions remain
separate. The fixture manifest pins both profiles and classifications for P1.
