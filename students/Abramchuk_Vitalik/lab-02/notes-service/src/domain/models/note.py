# domain/models/note.py
class Note:
    """Доменная модель: заметка"""
    def __init__(self, note_id: str, title: str, content: str):
        self.id = note_id
        self.title = title
        self.content = content
        self.tags = []