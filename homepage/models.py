from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

def image_directory_path(instance, filename):
    return 'images/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

class Art(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100, verbose_name='title')
    date = models.DateTimeField(auto_now_add=True, verbose_name='date')
    image = models.ImageField(upload_to=image_directory_path, verbose_name='image')
    description = models.TextField(null=True, blank=True, verbose_name='description')

    class Meta:
        verbose_name_plural='Art'

    def __str__(self):
        return self.title


# class Movie(models.Model):
#     url = models.URLField()
#
#     class Meta:
#         verbose_name_plural='Movie'
#
#
# class Music():
#     url = models.URLField()
#
#     class Meta:
#         verbose_name_plural = 'Music'