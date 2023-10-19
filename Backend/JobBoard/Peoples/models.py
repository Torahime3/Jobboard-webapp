from django.db import models
from Companies.models import Companies


# Create your models here.
# Model Peoples
# This model is used for the table Peoples

# This model contains :
#      - firstname : firstname of the people
#      - lastname : lastname of the people
#      - date_of_birth : date of birth of the people
#      - phone_number : phone number of the people
#      - email : email of the people
#      - domain : domain of the people
#      - url_profile_picture : url of the profile picture of the people
#      - role : role of the people
#      - id_company : id of the company
class Peoples(models.Model):
    RolesTypes = models.TextChoices("RolesTypes", "User Recruiter Admin")

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    url_profile_picture = models.CharField(max_length=255)
    role = models.CharField(blank=True,choices=RolesTypes.choices,max_length=10)
    id_company = models.ForeignKey(Companies, on_delete=models.CASCADE, null=True, blank=True)

    # Return the id of the People
    def __str__(self):
        return str(self.pk)

    # Rename the Peoples object for Django admin panel
    class Meta:
        verbose_name_plural = 'Peoples'
