from django.db import models
import datetime
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name