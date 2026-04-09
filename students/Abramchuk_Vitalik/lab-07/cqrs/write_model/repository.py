class InMemoryNoteRepository:
    def __init__(self):
        self.storage = {}

    def save(self, note):
        self.storage[note.note_id] = note

    def get(self, note_id):
        return self.storage.get(note_id)