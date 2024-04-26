from django.db import models

# Create your models here.

class GeneratedImage(models.Model):
    image_url = models.URLField()
    # text = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_url
