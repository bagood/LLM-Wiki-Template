from pathlib import Path

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from llm_wiki_mcp.domain.models import Model, Profile


class WikiRegistration(Model):
    wiki_id: str
    root: Path
    profile: Profile
    evidence_roots: list[Path] = Field(default_factory=list)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="LLM_WIKI_", extra="forbid")
    development_probe: bool = False
    index_path: Path = Path("artifacts/state/index.sqlite3")
    workflow_path: Path = Path("artifacts/state/workflows.sqlite3")
    wikis: list[WikiRegistration] = Field(default_factory=list)

    @model_validator(mode="after")
    def storage_outside_originals(self) -> Settings:
        if self.index_path.resolve() == self.workflow_path.resolve():
            raise ValueError("index and workflow databases require separate paths")
        roots = [
            root.resolve() for wiki in self.wikis for root in (wiki.root, *wiki.evidence_roots)
        ]
        for state_path in (self.index_path, self.workflow_path):
            if any(state_path.resolve().is_relative_to(root) for root in roots):
                raise ValueError(
                    "derived state must be outside registered knowledge/evidence roots"
                )
        if len({w.wiki_id for w in self.wikis}) != len(self.wikis):
            raise ValueError("wiki IDs must be unique")
        return self
