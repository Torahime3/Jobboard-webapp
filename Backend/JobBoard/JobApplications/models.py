from django.db import models
from JobAdvertisements.models import JobAdvertisements
from Peoples.models import Peoples

# Create your models here.
class JobApplications(models.Model):
    firstname = models.CharField(max_length=50, default="change_me")
    lastname = models.CharField(max_length=50, default="change_me")
    email = models.CharField(max_length=255, default="change_me")
    phone_number = models.CharField(max_length=10, default="000000")
    date_of_application = models.DateField()
    id_people = models.ForeignKey(Peoples, on_delete=models.CASCADE)
    id_advertisement = models.ForeignKey(JobAdvertisements, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'JobApplications'
