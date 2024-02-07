class FileObject:
    def __init__(self, id, bytes, created_at, filename, purpose, object_type="file"):
        self.id = id
        self.bytes = bytes
        self.created_at = created_at
        self.filename = filename
        self.purpose = purpose
        self.object_type = object_type

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            bytes=data.get('bytes'),
            created_at=data.get('created_at'),
            filename=data.get('filename'),
            purpose=data.get('purpose'),
            object_type=data.get('object')
        )