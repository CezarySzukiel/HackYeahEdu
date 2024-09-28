from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    homeworks = models.ManyToManyField('class_group_management.Homework', through='class_group_management.HomeworkAssignment')
    class_group = models.ForeignKey('class_group_management.ClassGroup', on_delete=models.CASCADE)

    def __str__(self):
        return self.username
