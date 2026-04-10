# services/notes_service.py
import uuid

class NotesService:
    def __init__(self):
        self.notes = {}

    def create_note(self, notebook_id, author_id, content):
        note_id = str(uuid.uuid4())
        note = {
            "note_id": note_id,
            "notebook_id": notebook_id,
            "author_id": author_id,
            "content": content
        }
        self.notes[note_id] = note
        return note

    def get_note(self, note_id):
        return self.notes.get(note_id)

    def stream_notes(self, notebook_id):
        for note in self.notes.values():
            if note["notebook_id"] == notebook_id:
                yield note