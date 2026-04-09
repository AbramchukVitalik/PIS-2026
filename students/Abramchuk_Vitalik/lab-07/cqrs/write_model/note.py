import uuid
from datetime import datetime
from cqrs.write_model.events import NoteCreated, NoteEdited


class Note:
    def __init__(self, note_id: str, notebook_id: str, author_id: str, content: str):
        self.note_id = note_id
        self.notebook_id = notebook_id
        self.author_id = author_id
        self.content = content
        self.history = []
        self._events = []

    @staticmethod
    def create(notebook_id: str, author_id: str, content: str):
        note = Note(
            note_id=str(uuid.uuid4()),
            notebook_id=notebook_id,
            author_id=author_id,
            content=content
        )

        event = NoteCreated(
            note.note_id,
            notebook_id,
            author_id,
            content,
            datetime.utcnow()
        )

        note._events.append(event)
        return note

    def edit(self, user_id: str, new_content: str):
        self.history.append(self.content)
        self.content = new_content

        event = NoteEdited(
            self.note_id,
            new_content,
            user_id,
            datetime.utcnow()
        )

        self._events.append(event)

    def pull_events(self):
        events = self._events[:]
        self._events.clear()
        return events