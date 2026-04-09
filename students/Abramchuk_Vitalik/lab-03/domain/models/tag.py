from dataclasses import dataclass


@dataclass(frozen=True)
class Tag:
    """Value Object: Метка заметки"""
    name: str

    def __post_init__(self):
        if not self.name or len(self.name.strip()) < 2:
            raise ValueError("Tag name must contain at least 2 characters")