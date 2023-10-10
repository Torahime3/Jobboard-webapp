from django.db import models
from Companies.models import Companies
from Peoples.models import Peoples

# Create your models here.
class JobAdvertisements(models.Model):
    types = models.TextChoices("Types", "CDD CDI Stage Alternance Saisonnier Été")

    title = models.CharField(max_length=255)
    job_domain = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_of_jobadvertisements = models.DateField()
    location = models.CharField(max_length=255)
    contract_type = models.CharField(blank=True,choices=types.choices,max_length=10)
    duration_week = models.CharField(max_length=50)
    id_company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    id_people = models.ForeignKey(Peoples, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'JobAdvertisements'