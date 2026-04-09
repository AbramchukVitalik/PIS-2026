class CreateNoteCommand:
    def __init__(self, notebook_id: str, author_id: str, content: str):
        if not notebook_id:
            raise ValueError("notebook_id is required")
        if not author_id:
            raise ValueError("author_id is required")
        if not content:
            raise ValueError("content is required")

        self.notebook_id = notebook_id
        self.author_id = author_id
        self.content = content