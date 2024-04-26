from django.shortcuts import render
from .tasks import generate_image

# from celery.result import AsyncResult

def generate_images(request):
    texts = ["A red flying dog", "A husky ninja", "A footballer kid", "A wizard on Mars", "Baby Dragon"]
    image_urls = []

    for text in texts:
        result = generate_image.delay(text)
        image_urls.append(result)

    return render(request, 'generated_images.html', {'image_urls': image_urls})
