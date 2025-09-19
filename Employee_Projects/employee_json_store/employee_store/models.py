from dataclasses import dataclass, field, asdict

@dataclass(slots=True)
class Employee:
    id: int
    name: str
    department: str
    salary: float = 0.0
    tags: list[str] = field(default_factory=list)