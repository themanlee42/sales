# messages_api.py
import openai
from .models.message import MessageObject
from .base_api import BaseAPI

class MessagesAPI(BaseAPI):
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def create_message(self, thread_id, role, content, file_ids=[], metadata={}):
        response = self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role=role,
            content=content,
            file_ids=file_ids,
            metadata=metadata
        )
        return MessageObject.from_dict(self._process_response(response))

    def list_messages(self, thread_id, limit=20, order='desc', after=None, before=None):
        response = self.client.beta.threads.messages.list(
            thread_id=thread_id,
            limit=limit,
            order=order,
            after=after,
            before=before
        )
        return [MessageObject.from_dict(self._process_response(msg)) for msg in response['data']]

    def retrieve_message(self, thread_id, message_id):
        response = self.client.beta.threads.messages.retrieve(
            thread_id=thread_id,
            message_id=message_id
        )
        return MessageObject.from_dict(self._process_response(response))