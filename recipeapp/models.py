from django.db import models

# Create your models here.

class CreateRecipe(models.Model):
    Name = models.CharField(max_length=60)
    Detail = models.TextField(max_length=500)
    Date = models.DateTimeField(null=True)