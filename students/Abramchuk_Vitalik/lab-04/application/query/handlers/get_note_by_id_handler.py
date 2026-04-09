from application.query.get_note_by_id_query import GetNoteByIdQuery
from application.port.out.note_repository import NoteRepository


class GetNoteByIdHandler:
    def __init__(self, repository: NoteRepository):
        self.repository = repository

    def handle(self, query: GetNoteByIdQuery):
        note = self.repository.find_by_id(query.note_id)

        if not note:
            return None

        # Read model (DTO-like dict)
        return {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "history": getattr(note, "history", [])
        }