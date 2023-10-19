from django.urls import path

from . import views

urlpatterns = [
    path("create", views.create, name="create"),
    path("", views.get_all_applications, name="all"),
    path("<int:id>", views.get_application_by_id, name="id"),
    path("<str:token>", views.get_application_by_token, name="token"), 
    path("<str:token>/company", views.get_application_by_id_company, name="company"),
    path('<str:token>/update', views.update, name="update"),
    path('<str:token>/delete', views.delete, name='delete'),
]
