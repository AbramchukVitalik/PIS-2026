class FakeNoteRepository:
    def __init__(self):
        self.storage = {}

    def save(self, note):
        self.storage[note.note_id] = note
        return note

    def find_by_id(self, note_id: str):
        return self.storage.get(note_id)