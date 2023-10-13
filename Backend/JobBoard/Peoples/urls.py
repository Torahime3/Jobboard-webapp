from django.urls import path

from . import views

urlpatterns = [
    #path('', views.get_peoples, name='all'),
    path('create', views.create, name='create'),
    path('update', views.create, name='update'),
    path('delete', views.create, name='delete'),
    path('<str:token>', views.get_people_by_token, name='token'),
]

