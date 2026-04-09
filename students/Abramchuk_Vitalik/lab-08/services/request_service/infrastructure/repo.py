# services/request_service/infrastructure/repo.py
class InMemoryNoteRepository:
    def __init__(self):
        self.db = {}

    def save(self, note):
        self.db[note.id] = note

    def get(self, note_id: str):
        return self.db.get(note_id)