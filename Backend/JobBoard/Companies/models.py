from django.db import models


# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    url_website = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Companies'