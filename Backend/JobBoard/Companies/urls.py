from django.urls import path
from . import views


urlpatterns = [
      path('<int:id>', views.getCompanyById, name='company'),
      path('<str:token>', views.getCompanyWithToken, name='all')
]
