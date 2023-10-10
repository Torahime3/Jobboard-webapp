from django.contrib import admin
# Register your models here.
from .models import JobApplications


class JobApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_application', 'id_advertisement_id', 'id_people_id')

admin.site.register(JobApplications, JobApplicationsAdmin)