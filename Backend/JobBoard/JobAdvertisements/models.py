from django.db import models
from Companies.models import Companies
from Peoples.models import Peoples

# Create your models here.
# Model JobAdvertisements
# This model is used for the table JobAdvertisements

# This model contains :
#       - title : title of the job
#       - job_domain : domain of the job
#       - description : description of the job
#       - date_of_jobadvertisements : date of the job
#       - location : location of the job
#       - contract_type : type of the contract, it can be CDD, CDI, Stage, Alternance, Saisonnier, Été
#       - duration_week : duration of the contract
#       - id_company : id of the company who publish the job advertisement
#       - id_people : id of the people who publish the job advertisement
class JobAdvertisements(models.Model):
    types = models.TextChoices("Types", "CDD CDI Stage Alternance Saisonnier Été")

    title = models.CharField(max_length=255)
    job_domain = models.CharField(max_length=100)
    description = models.CharField(max_length=65535)
    date_of_jobadvertisements = models.DateField()
    location = models.CharField(max_length=255)
    contract_type = models.CharField(blank=True,choices=types.choices,max_length=10)
    duration_week = models.CharField(max_length=50)
    id_company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    id_people = models.ForeignKey(Peoples, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = 'JobAdvertisements'