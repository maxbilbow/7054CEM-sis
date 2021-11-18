from dataclasses import dataclass, field


@dataclass(frozen=True, eq=True)
class User:
    id: int = field(metadata={"Key": True})
    email: str
    password_hash: str

