from django.urls import path
from . import views

urlpatterns = [
    path('test', views.get_company_by_id, name='get_company_by_id'),
]
