from django.contrib import admin
from .models import Peoples

# This class is used to display the table Peoples in the Django admin panel
class PeoplesAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'date_of_birth', 'phone_number', 'email', 'domain', 'url_profile_picture', 'role', 'id_company')

admin.site.register(Peoples, PeoplesAdmin)
