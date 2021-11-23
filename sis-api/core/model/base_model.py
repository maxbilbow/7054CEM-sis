from core.model import to_dict


class BaseModel:

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def to_dict(self):
        return to_dict(self)
