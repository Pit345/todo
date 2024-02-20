from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.username = self.username.capitalize()
        super().save(*args, **kwargs)