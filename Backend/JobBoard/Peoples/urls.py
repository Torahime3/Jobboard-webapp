from django.urls import path

from . import views

urlpatterns = [
    #path('', views.get_peoples, name='all'),
    path('<str:token>', views.get_people_by_token, name='token'),
    path('create', views.create_people, name='create_people'),
]
