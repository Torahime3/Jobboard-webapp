from django.contrib import admin
from .models import Login

# Settings for Django admin panel
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'token', 'id_people')

admin.site.register(Login,LoginAdmin)