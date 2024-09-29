from django.db import models
from users.models import CustomUser


class Homework(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ManyToManyField(CustomUser, through='HomeworkAssignment')

    def __str__(self):
        return self.title


class HomeworkAssignment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)


class ClassGroup(models.Model):
    name = models.CharField(max_length=2)
    homeroom_teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


