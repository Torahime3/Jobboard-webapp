from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('companies/', include('Companies.urls')),
    path('jobApplications/', include('JobApplications.urls')),
    path('jobAdvertisements/', include('JobAdvertisements.urls')),
    path('peoples/', include('Peoples.urls')),
    path('admin/', admin.site.urls),
]

