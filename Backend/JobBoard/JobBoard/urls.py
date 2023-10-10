from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('companies/',include('Companies.urls')),
    path('peoples/', include('Peoples.urls')),
    path('admin/', admin.site.urls),
]

