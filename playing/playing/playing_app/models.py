from django.db import models

# Create your models here.

class Responsible(models.Model):
    responsible_name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.responsible_name
    
    

class Todo(models.Model):
    todo_text = models.CharField(max_length = 200)
    todo_done = models.BooleanField()
    todo_created = models.DateField(auto_now = True)
    todo_responsibles = models.ManyToManyField(Responsible)
