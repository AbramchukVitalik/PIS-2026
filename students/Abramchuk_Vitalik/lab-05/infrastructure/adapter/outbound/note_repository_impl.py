from application.port.out.note_repository import NoteRepository
from infrastructure.persistence.models import NoteModel
from domain.models.note import Note
from infrastructure.config.database import SessionLocal


class NoteRepositoryImpl(NoteRepository):

    def save(self, note: Note):
        session = SessionLocal()

        db_note = NoteModel(
            id=note.id,
            title=note.title,
            content=note.content
        )

        session.merge(db_note)
        session.commit()
        session.close()

    def find_by_id(self, note_id: str):
        session = SessionLocal()

        db_note = session.query(NoteModel).filter_by(id=note_id).first()
        session.close()

        if not db_note:
            return None

        note = Note(db_note.title, db_note.content)
        note.id = db_note.id

        return note