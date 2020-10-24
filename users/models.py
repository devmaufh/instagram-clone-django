"""Users models """
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profile model

    Proxy model that extends the base data from other information.
    """

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    website = models.URLField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return username """
        return self.user.username
