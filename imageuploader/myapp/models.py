from django.db import models
#
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)


class BlogPost(models.Model):
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def number_of_likes(self):
        return self.likes.count()
