from django.db import models
from JobAdvertisements.models import JobAdvertisements
from Peoples.models import Peoples

# Create your models here.
# Model JobApplications
# This model is used for the table JobApplications

# This model contains :
#      - firstname : firstname of the people who apply to the job
#      - lastname : lastname of the people who apply to the job
#      - email : email of the people who apply to the job
#      - phone_number : phone number of the people who apply to the job
#      - date_of_application : date of the application
#      - id_people : id of the people who apply to the job
#      - id_advertisement : id of the job advertisement
class JobApplications(models.Model):
    firstname = models.CharField(max_length=50, default="change_me")
    lastname = models.CharField(max_length=50, default="change_me")
    email = models.CharField(max_length=255, default="change_me")
    phone_number = models.CharField(max_length=10, default="000000")
    date_of_application = models.DateField()
    id_people = models.ForeignKey(Peoples, on_delete=models.CASCADE)
    id_advertisement = models.ForeignKey(JobAdvertisements, on_delete=models.CASCADE)

# Rename the JobApplications object for Django admin panel
    class Meta:
        verbose_name_plural = 'JobApplications'
