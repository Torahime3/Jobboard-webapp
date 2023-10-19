from django.db import models
from Peoples.models import Peoples

# Model JobApplications
# This model is used for the table JobApplications
# This model contains :
#      - username : username of the people who connect to the website
#      - password : password of the people who connect to the website
#      - email : email of the people who connect to the website (used for connection)
#      - token : token of the people who connect to the website (used for connection)
#      - id_people : id of the people who connect to the website (reference to Peoples table)
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=50,default="token_to_change")
    id_people = models.ForeignKey(Peoples, on_delete=models.CASCADE)

    # Rename the Login object for Django admin panel
    class Meta:
        verbose_name_plural = 'Login'