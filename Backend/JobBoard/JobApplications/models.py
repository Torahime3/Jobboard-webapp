from django.db import models
from JobAdvertisements.models import JobAdvertisements
from Peoples.models import Peoples

# Create your models here.
class JobApplications(models.Model):
    types = models.TextChoices("Types", "CDD CDI Stage Alternance Saisonnier Été")

    id_people = models.ForeignKey(Peoples, on_delete=models.CASCADE)
    id_advertisement = models.ForeignKey(JobAdvertisements, on_delete=models.CASCADE)
    date_of_application = models.DateField()

    class Meta:
        verbose_name_plural = 'JobApplications'
