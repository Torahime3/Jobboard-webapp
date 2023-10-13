from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_applications, name='all'),
    path('<int:id>', views.get_application_by_id, name='id'),
    path('create', views.create, name='create'),
]
