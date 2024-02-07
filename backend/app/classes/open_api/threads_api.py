# threads_api.py
from .models.thread import ThreadObject
from .base_api import BaseAPI

class ThreadsAPI(BaseAPI):
    def __init__(self, api_key):
        super().__init__(api_key=api_key)

    def create_thread(self, messages=[], metadata={}):
        response = self.client.beta.threads.create(
            messages=messages,
            metadata=metadata
        )
        return ThreadObject.from_dict(self._process_response(response))

    def retrieve_thread(self, thread_id):
        response = self.client.beta.threads.retrieve(thread_id)
        return ThreadObject.from_dict(self._process_response(response))

    def modify_thread(self, thread_id, metadata):
        response = self.client.beta.threads.update(
            thread_id,
            metadata=metadata
        )
        return ThreadObject.from_dict(self._process_response(response))

    def delete_thread(self, thread_id):
        response = self.client.beta.threads.delete(thread_id)
        return self._process_response(response) 
