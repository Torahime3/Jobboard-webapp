from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all_applications, name="all"),
    path("create", views.create, name="create"),
    path("<int:id>", views.get_application_by_id, name="id"),
    path("<str:token>", views.get_application_by_token, name="token"),
]
