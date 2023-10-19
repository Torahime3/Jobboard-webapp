from django.urls import path
from . import views

# All urls for Login
# localhost:8000/login/
urlpatterns = [
    path('checkValidity', views.checkValidity, name='checKValidity'),
    path('checkAdmin', views.checkAdmin, name="checkAdmin"),
    path('<str:token>/all', views.getAll, name="get_all"),
    path('<str:token>/update', views.update, name='update'),
    path('<str:token>/delete', views.delete, name='delete'),
]
