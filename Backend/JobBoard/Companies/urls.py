from django.urls import path
from . import views

# Urls for the Companies app
# localhost:8000/companies/
urlpatterns = [
      path('<int:id>', views.getCompanyById, name='company'),
      path('<str:token>', views.getAll, name='companywithToken'),
      path('<str:token>/delete', views.delete, name='delete'),
      path('<str:token>/create', views.create, name='create'),
      path('<str:token>/update', views.update, name='update'),
]
