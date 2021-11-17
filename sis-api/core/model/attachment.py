from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Attachment:
    claim_note_id: int
    name: str
    mime_type: str
    data: bytes
