from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DomainEvent:
    occurred_at: datetime


@dataclass(frozen=True)
class NoteCreated(DomainEvent):
    note_id: str
    notebook_id: str
    author_id: str


@dataclass(frozen=True)
class NoteEdited(DomainEvent):
    note_id: str
    editor_id: str


@dataclass(frozen=True)
class TagAddedToNote(DomainEvent):
    note_id: str
    tag_name: str