from dataclasses import dataclass

@dataclass(frozen=True)
class CreateNoteCommand:
    title: str
    content: str

    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be blank")
        if not self.content or not self.content.strip():
            raise ValueError("Content cannot be blank")