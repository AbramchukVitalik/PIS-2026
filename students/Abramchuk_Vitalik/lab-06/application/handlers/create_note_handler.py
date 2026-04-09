from domain.note import Note


class CreateNoteHandler:
    def __init__(self, repository):
        self.repository = repository

    def handle(self, command):
        note = Note.create(
            notebook_id=command.notebook_id,
            author_id=command.author_id,
            content=command.content
        )

        return self.repository.save(note)