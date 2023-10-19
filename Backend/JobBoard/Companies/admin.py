from django.contrib import admin
from .models import Companies

# Settings for Django admin panel
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'address', 'city', 'zipcode', 'url_website')

admin.site.register(Companies,CompaniesAdmin)
