from django.contrib import admin

# Register your models here.
from .models import Peoples

class PeoplesAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'date_of_birth', 'phone_number', 'email', 'domain', 'url_profile_picture', 'role', 'id_company')

admin.site.register(Peoples, PeoplesAdmin)
