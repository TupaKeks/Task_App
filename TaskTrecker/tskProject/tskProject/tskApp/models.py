from django.db import models
from datetime import time

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    timer = models.TimeField(default=time(0,0,0))
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title