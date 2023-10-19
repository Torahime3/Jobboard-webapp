from django.urls import path
from . import views

# All urls for Peoples
# localhost:8000/peoples/
urlpatterns = [
    path('<str:token>/all', views.get_peoples, name="get_all"),
    path('<str:token>/create', views.create, name='create'),
    path('<str:token>/update', views.update, name='update'),
    path('<str:token>/delete', views.delete, name='delete'),
    path('<str:token>', views.get_people_by_token, name='token'),
    path('upload_img', views.download_img, name="upload_img")
]

