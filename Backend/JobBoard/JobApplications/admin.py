from django.contrib import admin
# Register your models here.
from .models import JobApplications


class JobApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'phone_number', 'id_advertisement_id', 'id_people_id', 'date_of_application')

admin.site.register(JobApplications, JobApplicationsAdmin)