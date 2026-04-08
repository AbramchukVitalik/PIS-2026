# domain/models/notebook.py
class Notebook:
    """Доменная модель: блокнот"""
    def __init__(self, notebook_id: str, name: str):
        self.id = notebook_id
        self.name = name
        self.notes = []