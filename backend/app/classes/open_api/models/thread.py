class ThreadObject:
    def __init__(self, id, created_at, metadata):
        self.id = id
        self.created_at = created_at
        self.metadata = metadata

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            created_at=data.get('created_at'),
            metadata=data.get('metadata', {})
        )