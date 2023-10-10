from django.db import models
from Companies.models import Companies

# Create your models here.
class Peoples(models.Model):
    url_profile_picture = models.CharField(max_length=255)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    id_company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)