from cqrs.read_model.note_view import NoteView
from cqrs.write_model.events import NoteCreated, NoteEdited


class NoteProjection:
    def __init__(self):
        self.views = {}

    def handle(self, event):
        if isinstance(event, NoteCreated):
            self.views[event.note_id] = NoteView(
                note_id=event.note_id,
                notebook_id=event.notebook_id,
                author_id=event.author_id,
                content=event.content,
                last_updated=event.created_at
            )

        elif isinstance(event, NoteEdited):
            view = self.views.get(event.note_id)
            if view:
                view.content = event.content
                view.last_updated = event.edited_at

    def get(self, note_id):
        return self.views.get(note_id)