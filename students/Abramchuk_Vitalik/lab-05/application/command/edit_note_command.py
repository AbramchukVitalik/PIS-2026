from dataclasses import dataclass

@dataclass(frozen=True)
class EditNoteCommand:
    note_id: str
    editor: str
    new_content: str

    def __post_init__(self):
        if not self.note_id:
            raise ValueError("note_id is required")
        if not self.editor:
            raise ValueError("editor is required")
        if not self.new_content or not self.new_content.strip():
            raise ValueError("content cannot be blank")