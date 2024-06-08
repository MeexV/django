from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ParsUser(AbstractUser):
    email = models.EmailField(unique=True)
