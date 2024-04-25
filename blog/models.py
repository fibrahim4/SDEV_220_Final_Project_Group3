from django.db import models
from django.conf import settings

# Create your models here.
class Inventory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='10000')
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.FloatField()
    status = models.TextField()
    
    def __str__(self):
        return self.name
