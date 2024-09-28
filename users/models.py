from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    class_group = models.ForeignKey('class_group_management.ClassGroup', on_delete=models.CASCADE, null=True,
                                    blank=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions', blank=True)

    def __str__(self):
        return self.username
