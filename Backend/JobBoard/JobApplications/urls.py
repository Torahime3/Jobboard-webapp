from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_applications, name='all'),
]
