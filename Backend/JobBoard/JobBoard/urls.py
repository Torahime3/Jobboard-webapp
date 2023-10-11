from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('companies/', include('Companies.urls')),
    path('jobapplications/', include('JobApplications.urls')),
    path('jobadvertisements/', include('JobAdvertisements.urls')),
    path('peoples/', include('Peoples.urls')),
    path('login/', include('Login.urls')),
    path('admin/', admin.site.urls),
]

