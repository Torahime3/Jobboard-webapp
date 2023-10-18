from django.contrib import admin

# Register your models here.
from .models import JobAdvertisements

# Setup for the admin page of JobAdvertisements
class JobAdvertisementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'job_domain', 'description', 'date_of_jobadvertisements', 'location', 'contract_type', 'duration_week', 'id_company_id', 'id_people_id')
admin.site.register(JobAdvertisements, JobAdvertisementsAdmin)
