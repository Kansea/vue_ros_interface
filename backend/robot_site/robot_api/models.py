from django.db import models

# Create your models here.
class Add(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    result = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
