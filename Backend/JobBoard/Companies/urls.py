from django.urls import path
from . import views


urlpatterns = [
      path('', views.getData, name='index'),
      path('<int:id>', views.getCompanyById, name='company')
]
