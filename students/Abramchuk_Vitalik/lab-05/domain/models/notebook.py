class Notebook:
    """Entity: Тетрадь"""

    def __init__(self, notebook_id: str, owner_id: str, title: str):
        if not title:
            raise ValueError("Notebook title cannot be empty")

        self._id = notebook_id
        self._owner_id = owner_id
        self._title = title
        self._notes_ids: list[str] = []

    @property
    def id(self):
        return self._id

    def add_note(self, note_id: str):
        if note_id in self._notes_ids:
            raise ValueError("Note already in notebook")
        self._notes_ids.append(note_id)

    def __eq__(self, other):
        return isinstance(other, Notebook) and self._id == other._id

    def __hash__(self):
        return hash(self._id)