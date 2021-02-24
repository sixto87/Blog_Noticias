from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nacionalidad = models.CharField(max_length = 30, null=True)
    pass
# Create your models here.
