# P0 runtime and compatibility

Owner and reviewer: repository owner (the requesting user). Implementation:
Codex. Owner-selected target AI hosts: Microsoft Copilot and Codex. Review acceptance
is recorded independently from automated checks in the phase report.

Baseline: CPython 3.14.8, standard GIL build; official MCP SDK 2.3.0;
requires-python `>=3.14,<3.15`; uv 0.13.0. Exact transitive dependency versions and
hashes are in `mcp-server/uv.lock`. The older locally installed uv could not discover
3.14.8; development bootstrapped a current uv in temporary storage. CI pins uv.
Stable runtime releases were checked against [Python downloads](https://www.python.org/downloads/)
and the SDK against its [package metadata](https://pypi.org/project/mcp/2.3.0/) and
[official v2 documentation](https://py.sdk.modelcontextprotocol.io/).

| Target | Behavior | P0 evidence | Remaining release qualification |
|---|---|---|---|
| MCP 2026-07-28 | discovery, self-contained calls, metadata/header checks | official Client mode auto against real Uvicorn | independent host and ingress |
| MCP 2025-11-25 | initialize, legacy calls/sessions | official Client mode legacy against real Uvicorn | actual host compatibility |
| FastAPI mount | manager lifecycle, canonical /mcp, no slash redirects | repeated startup/shutdown and path tests | production auth/readiness |
| Python 3.14.8 | locked install, lint/type/tests, FTS5 | environment.json, install.log, tests.xml | P4 container on pinned image |
| Python 3.15 | not supported by this release | NOT_RUN | qualification branch/job then installation, tests, container |
| Microsoft Copilot | owner-selected target; product/connector variant pending | NOT_RUN | MCP adapter/connector capability, test account, remote authorization |
| Codex | owner-selected target | NOT_RUN | connected test account, remote authorization and P5 workflow |

Follow the [SDK mounting](https://py.sdk.modelcontextprotocol.io/run/asgi/) and
[legacy-client guidance](https://py.sdk.modelcontextprotocol.io/run/legacy-clients/).
Local protocol proof does not establish cloud interoperability.

Python 3.15 qualification uses a separate `qualification/python-315` branch: widen
requires-python to `<3.16` there, set .python-version to a stable 3.15 patch, regenerate
the lock deliberately, run the same clean-install/check suite on Linux and macOS,
and build/test the P4 container before merging support. Do not bypass the current
interpreter constraint or label an unexecuted qualification PASS. Review patch
updates regularly and the next stable minor annually.

OAuth/OIDC service, public hostname, HTTPS ingress, hosting platform, secrets and
test-account access are pending owner selection/provisioning for P4/P5. Planned
integration uses an external OAuth/OIDC issuer and a resource-server verifier
(issuer/audience/expiry/scopes), with a single worker and separate persistent state
volumes. No provider model key is a normal server dependency. CI and Docker jobs
not executed locally remain NOT_RUN in evidence, not inferred successful.
