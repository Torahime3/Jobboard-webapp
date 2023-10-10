from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('my_api.urls')),
    path('my_api/', include('my_api.urls')),
    path('Companies/',include('Companies.urls')),
    path('admin/', admin.site.urls),
]

