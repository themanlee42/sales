class ImageObject:
    def __init__(self, url, revised_prompt=None):
        self.url = url
        self.revised_prompt = revised_prompt

    @classmethod
    def from_dict(cls, data):
        return cls(
            url=data.get('url'),
            revised_prompt=data.get('revised_prompt')
        )