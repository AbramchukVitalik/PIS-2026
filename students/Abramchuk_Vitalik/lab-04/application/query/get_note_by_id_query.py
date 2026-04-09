from dataclasses import dataclass

@dataclass(frozen=True)
class GetNoteByIdQuery:
    note_id: str