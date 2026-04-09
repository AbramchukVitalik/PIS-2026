from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class NoteHistoryEntry:
    """Value Object: Запись истории изменений"""
    editor_id: str
    content_snapshot: str
    edited_at: datetime