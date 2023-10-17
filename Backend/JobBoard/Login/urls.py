from django.urls import path
from . import views


urlpatterns = [
    path('checkValidity', views.checkValidity, name='checKValidity'),
    path('checkAdmin', views.checkAdmin, name="checkAdmin"),
    # path('<str:token>/all', views.get_peoples, name="get_all"),
    # path('<str:token>/create', views.create, name='create'),
    path('<str:token>/update', views.update, name='update'),
    path('<str:token>/delete', views.delete, name='delete'),
]
