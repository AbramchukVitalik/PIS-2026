import uuid
from domain.models.note import Note

class CreateNoteHandler:

    def __init__(self, note_repository):
        self.note_repository = note_repository

    def handle(self, command):
        note = Note(
            note_id=str(uuid.uuid4()),
            notebook_id=command.notebook_id,
            author_id=command.author_id,
            content=command.content
        )

        self.note_repository.save(note)
        return note.note_id