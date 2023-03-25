from django.db import models

# Create your models here.
class Data(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
class details(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(max_length=2000,null=True,default=None)
    country = models.CharField(max_length=2000)
    review = models.CharField(max_length=3000)
    ids = models.CharField(max_length=100)
class url1(models.Model):
    idss = models.CharField(max_length=200)
    urls = models.CharField(max_length=3000)
