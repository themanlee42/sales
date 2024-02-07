class RunObject:
    def __init__(self, id, thread_id, assistant_id, status, model, instructions, tools, file_ids, metadata, created_at=None, usage=None, last_error=None):
        self.id = id
        self.thread_id = thread_id
        self.assistant_id = assistant_id
        self.status = status
        self.model = model
        self.instructions = instructions
        self.tools = tools
        self.file_ids = file_ids
        self.metadata = metadata
        self.created_at = created_at
        self.usage = usage
        self.last_error = last_error

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            thread_id=data.get('thread_id'),
            assistant_id=data.get('assistant_id'),
            status=data.get('status'),
            model=data.get('model'),
            instructions=data.get('instructions'),
            tools=data.get('tools', []),
            file_ids=data.get('file_ids', []),
            metadata=data.get('metadata', {}),
            created_at=data.get('created_at'),
            usage=data.get('usage'),
            last_error=data.get('last_error')
        )