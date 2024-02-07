# files_api.py
import openai
from .base_api import BaseAPI
from .models.file import FileObject

class FilesAPI(BaseAPI):
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def upload_file(self, file_path, purpose):
        with open(file_path, 'rb') as file:
            response = self.client.files.create(
                file=file,
                purpose=purpose
            )
        return FileObject.from_dict(self._process_response(response))

    def list_files(self, purpose=None):
        response = self.client.files.list(purpose=purpose)
        return [FileObject.from_dict(self._process_response(file)) for file in response['data']]

    def retrieve_file(self, file_id):
        response = self.client.files.retrieve(file_id)
        return FileObject.from_dict(self._process_response(response))

    def delete_file(self, file_id):
        response = self.client.files.delete(file_id)
        return self._process_response(response)

    def retrieve_file_content(self, file_id):
        content = self.client.files.content(file_id)
        return self._process_response(content)
