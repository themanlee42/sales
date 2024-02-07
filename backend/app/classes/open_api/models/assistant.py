class AssistantObject:
    def __init__(self, id, name, model, instructions, tools, file_ids, metadata, created_at=None, description=None):
        self.id = id
        self.name = name
        self.model = model
        self.instructions = instructions
        self.tools = tools
        self.file_ids = file_ids
        self.metadata = metadata
        self.created_at = created_at
        self.description = description

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            model=data.get('model'),
            instructions=data.get('instructions'),
            tools=data.get('tools', []),
            file_ids=data.get('file_ids', []),
            metadata=data.get('metadata', {}),
            created_at=data.get('created_at'),
            description=data.get('description')
        )

class AssistantFileObject:
    def __init__(self, id, assistant_id, created_at):
        self.id = id
        self.assistant_id = assistant_id
        self.created_at = created_at

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            assistant_id=data.get('assistant_id'),
            created_at=data.get('created_at')
        )
