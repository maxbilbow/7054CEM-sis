from dataclasses import dataclass, field


@dataclass(frozen=True, eq=True)
class Quote:
    id: int = field(metadata={"Key": True})
    user_id: int
