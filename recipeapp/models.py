from django.db import models
from datetime import date

# Create your models here.

class CreateRecipe(models.Model):
    Name = models.CharField(max_length=100)
    Detail = models.TextField(max_length=2000)
    Date = models.DateField( ("DATE"), default = date.today)