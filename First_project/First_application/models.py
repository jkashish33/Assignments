from django.db import models

# Create your models here.

class first_model(models.Model):
    name = models.CharField(max_length = 20)
    id = models.IntegerField(default=0, primary_key = True)
    contact = models.IntegerField(default=0)
    address = models.CharField(max_length = 100)