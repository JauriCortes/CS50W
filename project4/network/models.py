from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Posts(models.Model):
    poster = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)