from django.contrib.auth.handlers.modwsgi import check_password
from django.db import models
from django.contrib.auth.hashers import make_password

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=255)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    class Meta:
        verbose_name_plural = 'Login'