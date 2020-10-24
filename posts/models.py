"""Post models"""
from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    """Post model"""

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # User foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Profile foreign key
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    def __str__(self):
        """Return title and post owner """
        return '{} by @{}'.format(self.title, self.user.username)
