# runs_api.py
from .models.run import RunObject
from .base_api import BaseAPI

class RunsAPI(BaseAPI):
    def __init__(self, api_key):
        super().__init__(api_key=api_key)

    def create_run(self, thread_id, assistant_id, model=None, instructions=None, additional_instructions=None, tools=None, metadata={}):
        response = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
            model=model,
            instructions=instructions,
            additional_instructions=additional_instructions,
            tools=tools,
            metadata=metadata
        )
        return RunObject.from_dict(self._process_response(response))

    def list_runs(self, thread_id, limit=20, order='desc', after=None, before=None):
        response = self.client.beta.threads.runs.list(
            thread_id=thread_id,
            limit=limit,
            order=order,
            after=after,
            before=before
        )
        return [RunObject.from_dict(self._process_response(run)) for run in response['data']]

    def retrieve_run(self, thread_id, run_id):
        response = self.client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        return RunObject.from_dict(self._process_response(response))