# services/request_service/application/create_note_handler.py
from domain.note import Note

class CreateNoteHandler:
    def __init__(self, repo, publisher):
        self.repo = repo
        self.publisher = publisher

    def handle(self, notebook_id, author_id, content):
        note = Note(notebook_id, author_id, content)

        self.repo.save(note)

        self.publisher.publish({
            "type": "NoteCreated",
            "note_id": note.id,
            "notebook_id": notebook_id
        })

        return note.id