from django.db import models

# Create your models here.
from djongo import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
