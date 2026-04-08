# domain/models/tag.py
class Tag:
    """Доменная модель: тег для заметки"""
    def __init__(self, name: str):
        self.name = name