# P0 acceptance corpus

`stock-analysis/` is a byte-for-byte copy of the supplied workspace excluding
macOS `.DS_Store` metadata. It is evidence, never executable instructions.
The original workspace remains authoritative and is never edited by the server.
`manifest.json` pins every fixture file and the ordered tree hash; it also records
all 28 accepted identities, the five BULL IDs, baseline counts, and candidate warnings.
Tests fail on drift. Updating a fixture requires an explicit reviewed manifest update;
the normal validation command never refreshes expected hashes.

`generic-okf/` has no workspace manifest or raw directory. `notes.md` deliberately
has only `type`; `experiment.md` has an unknown type/field and external provenance.
`reference-1` in the weather page and experiment identifies two distinct declarations.
The Unicode filename, reference link, aliases, hub, and reserved index/log are valid.
`missing.md` yields a warning. External resources remain unresolved references and
are never fetched. A navigation hub supplies no evidence votes.

`parser-cases/` contains valid cycles (a bounded traversal must terminate), malformed
YAML and duplicate keys (errors), and an unsafe YAML constructor (error, no execution).
Expected classifications and relationships are in the pinned fixture manifest.
P0 checks bytes/frontmatter classifications; full parser/link resolution lands in P1.
