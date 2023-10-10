from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Companies/',include('Companies.urls')),
    path('Peoples/', include('Peoples.urls')),
    path('admin/', admin.site.urls),
]

