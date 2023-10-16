from django.urls import path
from . import views


urlpatterns = [
    path('checkValidity', views.checkValidity, name='checKValidity'),
    path('checkAdmin', views.checkAdmin, name="checkAdmin"),
]
