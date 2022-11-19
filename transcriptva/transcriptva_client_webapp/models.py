from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    company = models.TextField(
        null=True,
        blank=True
    )