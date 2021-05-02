from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        get_absolute_url: After updating/editing/adding blog takes back to home.url
        return: home page
        """
        return reverse('home')


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    # Uploading images in automatically generated directories 'images/'
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        """
        get_absolute_url: After updating/editing/adding blog takes back to home.url
        return: home page
        """
        return reverse('home')
