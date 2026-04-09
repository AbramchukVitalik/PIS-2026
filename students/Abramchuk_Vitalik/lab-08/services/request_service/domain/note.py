# services/request_service/domain/note.py
import uuid
from datetime import datetime

class Note:
    def __init__(self, notebook_id: str, author_id: str, content: str):
        self.id = str(uuid.uuid4())
        self.notebook_id = notebook_id
        self.author_id = author_id
        self.content = content
        self.tags = []
        self.history = []
        self.created_at = datetime.utcnow()

    def edit(self, new_content: str):
        self.history.append(self.content)
        self.content = new_content