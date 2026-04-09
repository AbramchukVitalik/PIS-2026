from sqlalchemy import Column, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class NoteModel(Base):
    __tablename__ = "notes"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)