# images_api.py
import openai
from .models.image import ImageObject
from .base_api import BaseAPI

class ImagesAPI(BaseAPI):
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def create_image(self, prompt, model="dall-e-2", n=1, quality="standard", response_format="url", size="1024x1024", style="vivid", user=None):
        response = self.client.images.generate(
            model=model,
            prompt=prompt,
            n=n,
            quality=quality,
            response_format=response_format,
            size=size,
            style=style,
            user=user
        )
        return [ImageObject.from_dict(self._process_response(image)) for image in response['data']]

    def create_image_edit(self, image_path, prompt, mask_path=None, model="dall-e-2", n=1, size="1024x1024", response_format="url", user=None):
        with open(image_path, 'rb') as image:
            mask = open(mask_path, 'rb') if mask_path else None
            response = self.client.images.edit(
                image=image,
                mask=mask,
                prompt=prompt,
                model=model,
                n=n,
                size=size,
                response_format=response_format,
                user=user
            )
            if mask:
                mask.close()
        return [ImageObject.from_dict(self._process_response(image)) for image in response['data']]

    def create_image_variation(self, image_path, model="dall-e-2", n=1, response_format="url", size="1024x1024", user=None):
        with open(image_path, 'rb') as image:
            response = self.client.images.create_variation(
                image=image,
                model=model,
                n=n,
                response_format=response_format,
                size=size,
                user=user
            )
        return [ImageObject.from_dict(self._process_response(image)) for image in response['data']]