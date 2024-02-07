# base_api.py
class BaseAPI:
    def _process_response(self, response):
        if hasattr(response, 'dict'):
            return response.dict()
        return response
