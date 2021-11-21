class BaseModel:

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
