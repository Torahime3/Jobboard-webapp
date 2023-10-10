from django.contrib import admin

# Register your models here.
from .models import Companies

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'address', 'city', 'zipcode', 'url_website')

admin.site.register(Companies,CompaniesAdmin)
