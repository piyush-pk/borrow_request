from django.db import models

# Create your models here.
class Request(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    device_price = models.FloatField()
    details = models.TextField()
    token = models.CharField(max_length=150)
    approved = models.BooleanField(default = False)
    time = models.DateTimeField(auto_now_add=True)