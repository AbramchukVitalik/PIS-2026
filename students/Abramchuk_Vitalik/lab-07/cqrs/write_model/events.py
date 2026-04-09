from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class NoteCreated:
    note_id: str
    notebook_id: str
    author_id: str
    content: str
    created_at: datetime


@dataclass(frozen=True)
class NoteEdited:
    note_id: str
    content: str
    edited_by: str
    edited_at: datetime