from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200) 
    date = models.DateField() 
    description = models.TextField(max_length=1000) 

    def __str__(self):
        return self.title