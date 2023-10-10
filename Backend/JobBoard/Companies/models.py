from django.db import models


# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    url_website = models.CharField(max_length=255)
