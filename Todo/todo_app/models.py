from django.db import models

# Create your models here.
class Todo(models.Model):
    content =  models.CharField(max_length=255)
    priority = models.IntegerField(default=0)
    date = models.DateField(default='1111-11-11')
