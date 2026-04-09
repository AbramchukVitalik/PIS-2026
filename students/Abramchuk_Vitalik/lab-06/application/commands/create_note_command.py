class CreateNoteCommand:
    def __init__(self, notebook_id: str, author_id: str, content: str):
        if not notebook_id or not author_id:
            raise ValueError("Invalid ids")

        self.notebook_id = notebook_id
        self.author_id = author_id
        self.content = content