from celery import shared_task
import requests
from .models import GeneratedImage

@shared_task
def generate_image(text):
    try:
        url = 'https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image'
        payload = {'text': text}
        headers = {'Authorization': 'sk-q4uoFqg4J5qLWrriHWNIMUNCBKddtY6ZqngrsmXYybjZK3I2'}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  
        image_url = response.json().get('image_url')

        GeneratedImage.objects.create(image_url=image_url, text=text)

        return image_url
    
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
