# ADR 0001: Layered dependencies

Status: proposed for owner review; implemented in P0.

Controllers translate transport requests and resolve the container explicitly.
Services depend on domain objects and repository protocols. Repositories depend
on domain objects, with no tool descriptions, provider decisions, or controller imports.
Domain objects and contracts cannot import transport packages. The composition
root (`app.py`, `container.py`) wires layers and is not itself a domain dependency.

P0 defines storage ports but supplies no production repository or tool placeholders.
The real-package AST test includes absolute, relative, and literal dynamic imports
and rejects uninspectable dynamic imports. Provider SDK imports are forbidden.
P1 will compose concrete page/search/graph ports; P3 supplies workflow state.
