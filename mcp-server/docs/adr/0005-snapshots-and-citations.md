# ADR 0005: Snapshot reads and citation identity

Status: proposed for owner review; persistence is P1/P3.

Page identity is `(wiki_id, bundle_relative_path)`; public URIs are portable and
contain no host filesystem paths. Citations add a snapshot, page hash, section,
and original inclusive line/half-open UTF-8 byte spans. Provenance retains its
declaring page and resource URI. Template accepted source IDs are manifest scoped.

Snapshots retain indexed page bytes and approved raw excerpts needed by active
workflows. An old snapshot must never read newer filesystem bytes. Retention
failure produces SNAPSHOT_EXPIRED, and a workflow cannot silently repin. Refresh
never edits wiki/raw bytes; raw integrity failures quarantine evidence, while
page drift is a finding and not automatically an invalid manual edit.

A summary citation never implies the raw original was read. Raw URI/hash/span
require `raw_read: true`. Declaration, byte integrity, human verification,
semantic support, and independence are separate properties. Semantic support
remains `not_assessed` by these deterministic tools. Preserve original report
strings and constituent context sets alongside normalized values.

Continuation cursors are opaque authenticated payloads bound to principal,
operation, wiki, snapshot, canonical query/filter/budget hash, position, and expiry.
Mismatch is INVALID_CURSOR. Trim whole passages/hits, retain their citations,
declare omissions, and offer continuation; never silently cut citation records.
