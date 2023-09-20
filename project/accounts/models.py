from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CLIENT = "CLIENT", 'Client'

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.ADMIN)
    middle_name = models.CharField(max_length=50, null=True, blank=True)


