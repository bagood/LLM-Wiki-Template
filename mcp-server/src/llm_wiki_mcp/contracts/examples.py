"""Reviewable examples of future production calls, not registered handlers."""

from copy import deepcopy

from pydantic import JsonValue, TypeAdapter


def examples() -> dict[str, dict[str, JsonValue]]:
    scope = {"wiki_id": "garden", "snapshot_id": "snapshot-example"}
    uri = "wiki://garden/page/notes.md"
    span = {"start_line": 4, "end_line": 4}
    page = {
        **scope,
        "page_id": "notes.md",
        "uri": uri,
        "content_hash": "a" * 64,
        "type": "note",
        "markdown": "Garden notes.",
        "span": span,
        "total_lines": 4,
    }
    identity = {
        "provenance_id": "reference-1",
        "declaring_page_uri": uri,
        "resource_uri": "https://example.org/gardens/study",
    }
    citation = {
        **scope,
        "citation_id": "citation-1",
        "page_uri": uri,
        "page_hash": "a" * 64,
        "page_span": span,
    }
    node = {"page_id": "notes.md", "uri": uri, "type": "note"}
    counts = {"content_pages": 4, "sources": 0, "entities": 0, "concepts": 0, "overviews": 0}
    workflow = {
        **scope,
        "workflow_id": "workflow-1",
        "owner": "reader-1",
        "version": 1,
        "goal": "Compare garden observations",
        "state": "running",
        "steps": [{"step_id": "read", "description": "Read evidence"}],
        "budget": {},
        "created_at": "2026-10-12T00:00:00Z",
        "expires_at": "2026-10-13T00:00:00Z",
    }
    artifact = {"artifact_id": "answer-1", "kind": "answer", "text": "Evidence is limited."}
    job = {"job_id": "job-1", "wiki_id": "garden", "owner": "admin-1", "state": "queued"}
    passage = {
        "page_id": "notes.md",
        "markdown": "Garden notes.",
        "citation_ids": ["citation-1"],
        "contexts": [],
    }
    w_input = {"wiki_id": "garden", "workflow_id": "workflow-1"}
    mutation = {**w_input, "expected_version": 1, "idempotency_key": "example-key-1"}
    completed = deepcopy(workflow)
    completed["state"] = "completed"
    completed["version"] = 2
    completed["steps"] = [
        {"step_id": "read", "description": "Read evidence", "status": "completed"}
    ]
    cases = {
        "wiki_list": (
            {},
            {
                "wikis": [
                    {
                        "wiki_id": "garden",
                        "scope": "Garden observations",
                        "profile": "okf_bundle",
                        "okf_version": "0.2",
                        "capabilities": [],
                        "active_snapshot_id": "snapshot-example",
                        "counts": counts,
                    }
                ]
            },
        ),
        "wiki_overview": (
            {"wiki_id": "garden"},
            {
                "navigation": [node],
                "coverage": counts,
                "limitations": ["External originals unavailable"],
                "contexts": [],
                "candidates": [],
            },
        ),
        "wiki_search": (
            {**scope, "query": "garden"},
            {
                "hits": [
                    {
                        "page_id": "notes.md",
                        "section": None,
                        "uri": uri,
                        "snippet": "Garden notes.",
                        "score": 1.0,
                        "score_components": {"lexical": 1.0},
                        "citation_ids": ["citation-1"],
                        "contexts": [],
                    }
                ],
                "total_matches": 1,
            },
        ),
        "wiki_resolve": (
            {**scope, "label": "Notes"},
            {"matches": [node], "candidates": [], "ambiguous": False},
        ),
        "wiki_get_page": ({**scope, "page_id": "notes.md"}, {"page": page}),
        "wiki_get_pages": (
            {**scope, "page_ids": ["notes.md"]},
            {"results": [{"page_id": "notes.md", "page": page}], "complete": True},
        ),
        "wiki_get_evidence": (
            {**scope, "source_id": "reference-1", "declaring_page_id": "notes.md"},
            None,
        ),
        "wiki_neighbors": ({**scope, "page_id": "notes.md"}, {"nodes": [node], "edges": []}),
        "wiki_subgraph": (
            {**scope, "seed_ids": ["notes.md"]},
            {"nodes": [node], "edges": [], "visited_nodes": 1, "elapsed_ms": 0.5},
        ),
        "wiki_find_paths": (
            {**scope, "from_id": "notes.md", "to_id": "experiment.md"},
            {"paths": []},
        ),
        "wiki_provenance": (
            {**scope, "page_id": "notes.md"},
            {
                "chain": [],
                "evidence_identities": [identity],
                "dependence_caveats": ["Distinct IDs do not prove independence"],
            },
        ),
        "wiki_collect_context": (
            {**scope, "seed_ids": ["notes.md"]},
            {
                "passages": [passage],
                "evidence_identities": [],
                "limitations": [],
                "follow_up_candidates": [],
            },
        ),
        "wiki_compare": (
            {**scope, "page_ids": ["notes.md", "experiment.md"], "fields": ["type"]},
            {
                "cells": [],
                "structured_differences": [],
                "unresolved_semantic_questions": ["Do observations agree?"],
            },
        ),
        "wiki_check_coverage": (
            {**scope, "topic_ids": ["notes.md"]},
            {"cells": [], "complete": False},
        ),
        "wiki_check_citations": (
            {
                **scope,
                "claims": [
                    {
                        "claim_id": "claim-1",
                        "text": "There are garden notes.",
                        "citation_ids": ["citation-1"],
                    }
                ],
                "citations": [citation],
            },
            {
                "checks": [
                    {
                        "citation_id": "citation-1",
                        "exists": True,
                        "hash_matches": True,
                        "span_valid": True,
                        "identity_valid": True,
                        "context_matches": None,
                        "issues": [],
                    }
                ],
                "unresolved_claim_ids": [],
            },
        ),
        "workflow_create": (
            {
                **scope,
                "goal": "Compare garden observations",
                "template": "compare_reports",
                "idempotency_key": "example-key-1",
            },
            {"workflow": {**workflow, "state": "created"}, "next_eligible_step_ids": ["read"]},
        ),
        "workflow_get": (w_input, {"workflow": workflow, "next_eligible_step_ids": ["read"]}),
        "workflow_checkpoint": (
            {**mutation, "event": "start"},
            {"workflow": workflow, "next_eligible_step_ids": ["read"]},
        ),
        "workflow_finalize": (
            {**mutation, "answer": artifact},
            {
                "workflow": completed,
                "next_eligible_step_ids": [],
                "outcome": "completed",
                "gaps": [],
                "pages_used": [],
            },
        ),
        "workflow_cancel": (
            {**mutation, "reason": "Research cancelled"},
            {
                "workflow": {**workflow, "state": "cancelled", "version": 2},
                "next_eligible_step_ids": [],
            },
        ),
        "wiki_validate": (
            {"wiki_id": "garden"},
            {"scope": "bundle", "valid": True, "findings": []},
        ),
        "wiki_index_status": (
            {"wiki_id": "garden"},
            {
                "active_snapshot": None,
                "jobs": [],
                "failed_evidence_ids": [],
                "rebuild_needed": True,
            },
        ),
        "admin_rebuild_index": (
            {"wiki_id": "garden", "idempotency_key": "example-key-1"},
            {"job": job},
        ),
        "admin_get_job": ({"wiki_id": "garden", "job_id": "job-1"}, {"job": job}),
    }
    result: dict[str, object] = {}
    for name, (request, data) in cases.items():
        response = {
            "schema_version": "1.0",
            **scope,
            "data": data,
            "citations": [],
            "warnings": [],
            "truncated": False,
            "next_cursor": None,
            "error": None,
        }
        if name == "wiki_list":
            response.update(wiki_id=None, snapshot_id=None)
        if name in ("wiki_search", "wiki_collect_context", "wiki_check_citations"):
            response["citations"] = [citation]
        if name == "wiki_get_evidence":
            response["error"] = {
                "code": "EVIDENCE_UNAVAILABLE",
                "detail": "Bundle-only external original was not fetched",
                "retryable": False,
            }
        result[name] = {"input": request, "output": response}
    return TypeAdapter(dict[str, dict[str, JsonValue]]).validate_python(result)
