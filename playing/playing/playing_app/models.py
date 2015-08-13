from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Todo(models.Model):
    todo_text = models.CharField(max_length = 200)
    todo_done = models.NullBooleanField(null = True)
    todo_created = models.DateField(null = True)
    todo_responsibles = models.ManyToManyField(User)
