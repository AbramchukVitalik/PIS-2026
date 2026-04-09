from typing import Dict, Optional
from domain.models.note import Note


class InMemoryNoteRepository:
    """
    In-memory реализация репозитория заметок.
    Используется для тестов и локальной разработки.
    """

    def __init__(self):
        self.storage: Dict[str, Note] = {}

    # CREATE / UPDATE
    def save(self, note: Note) -> Note:
        self.storage[note.note_id] = note
        return note

    # READ by ID
    def find_by_id(self, note_id: str) -> Optional[Note]:
        return self.storage.get(note_id)

    # optional (если нужно в сервисе)
    def find_all(self):
        return list(self.storage.values())