from django.db import models
from Peoples.models import Peoples


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=50,default="token_to_change")
    id_people = models.ForeignKey(Peoples, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Login'