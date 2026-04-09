import uuid


class Note:
    def __init__(self, note_id: str, notebook_id: str, author_id: str, content: str):
        self.note_id = note_id
        self.notebook_id = notebook_id
        self.author_id = author_id
        self.content = content

    @staticmethod
    def create(notebook_id: str, author_id: str, content: str):
        if not content or len(content.strip()) == 0:
            raise ValueError("Empty content")

        return Note(
            note_id=str(uuid.uuid4()),
            notebook_id=notebook_id,
            author_id=author_id,
            content=content
        )