from dataclasses import dataclass, field, asdict
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def __post_init__(self):
        self.title = self.title.strip()
        if not self.title:
            raise ValueError("Task title cannot be empty.")

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(**data)