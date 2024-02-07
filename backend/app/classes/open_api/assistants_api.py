# assistants_api.py
import openai
from typing import List
from .models.assistant import AssistantFileObject, AssistantObject
from .base_api import BaseAPI

class AssistantsAPI(BaseAPI):
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def create_assistant(self, model, instructions, name=None, description=None, tools=[], file_ids=[], metadata={}) -> AssistantObject:
        response = self.client.beta.assistants.create(
            model=model,
            instructions=instructions,
            name=name,
            description=description,
            tools=tools,
            file_ids=file_ids,
            metadata=metadata
        )
        return AssistantObject.from_dict(self._process_response(response))

    def create_assistant_file(self, assistant_id, file_id) -> AssistantFileObject:
        response = self.client.beta.assistants.files.create(
            assistant_id=assistant_id,
            file_id=file_id
        )
        return AssistantFileObject.from_dict(self._process_response(response))

    def list_assistants(self, limit=20, order='desc', after=None, before=None) -> List[AssistantObject]:
        response = self.client.beta.assistants.list(
            limit=limit,
            order=order,
            after=after,
            before=before
        )
        return [AssistantObject.from_dict(self._process_response(item)) for item in response.data]

    def list_assistant_files(self, assistant_id, limit=20, order='desc', after=None, before=None) -> List[AssistantFileObject]:
        response = self.client.beta.assistants.files.list(
            assistant_id=assistant_id,
            limit=limit,
            order=order,
            after=after,
            before=before
        )
        return [AssistantFileObject.from_dict(self._process_response(item)) for item in response.data]

    def retrieve_assistant(self, assistant_id) -> AssistantObject:
        response = self.client.beta.assistants.retrieve(assistant_id)
        return AssistantObject.from_dict(self._process_response(response))

    def retrieve_assistant_file(self, assistant_id, file_id) -> AssistantFileObject:
        response = self.client.beta.assistants.files.retrieve(
            assistant_id=assistant_id,
            file_id=file_id
        )
        return AssistantFileObject.from_dict(self._process_response(response))

    def modify_assistant(self, assistant_id, **kwargs) -> AssistantObject:
        response = self.client.beta.assistants.update(
            assistant_id,
            **kwargs
        )
        return AssistantObject.from_dict(self._process_response(response))

    def delete_assistant(self, assistant_id):
        response = self.client.beta.assistants.delete(assistant_id)
        return self._process_response(response)

    def delete_assistant_file(self, assistant_id, file_id):
        response = self.client.beta.assistants.files.delete(
            assistant_id=assistant_id,
            file_id=file_id
        )
        return self._process_response(response)
