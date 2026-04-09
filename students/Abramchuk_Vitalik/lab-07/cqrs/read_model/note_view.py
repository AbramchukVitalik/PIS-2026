from dataclasses import dataclass
from datetime import datetime


@dataclass
class NoteView:
    note_id: str
    notebook_id: str
    author_id: str
    content: str
    last_updated: datetime