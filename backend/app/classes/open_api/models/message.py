class MessageObject:
    def __init__(self, id, thread_id, role, content, file_ids=[], assistant_id=None, run_id=None, metadata={}, created_at=None):
        self.id = id
        self.thread_id = thread_id
        self.role = role
        self.content = content
        self.file_ids = file_ids
        self.assistant_id = assistant_id
        self.run_id = run_id
        self.metadata = metadata
        self.created_at = created_at

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            thread_id=data.get('thread_id'),
            role=data.get('role'),
            content=data.get('content'),
            file_ids=data.get('file_ids', []),
            assistant_id=data.get('assistant_id'),
            run_id=data.get('run_id'),
            metadata=data.get('metadata', {}),
            created_at=data.get('created_at')
        )
