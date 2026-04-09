class NoteService:

    def __init__(self, repository):
        self.repository = repository

    def create_note(self, command):
        import uuid
        from domain.models.note import Note

        note = Note(
            note_id=str(uuid.uuid4()),
            notebook_id=command.notebook_id,
            author_id=command.author_id,
            content=command.content
        )

        self.repository.save(note)
        return note.note_id

    # ✅ ВОТ ЭТОГО НЕ ХВАТАЕТ
    def get_note(self, note_id: str):
        note = self.repository.find_by_id(note_id)

        if not note:
            raise ValueError("Note not found")

        return note