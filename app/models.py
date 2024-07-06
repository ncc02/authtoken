from django.db import models
from django.contrib.auth.models import AbstractUser

class Blog(models.Model):
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ['-created']
# Create your models here.

