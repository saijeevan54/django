

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    assignees = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    assignee = models.OneToOneField(
        User, to_field='username', on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, to_field='name', related_name='project_tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
