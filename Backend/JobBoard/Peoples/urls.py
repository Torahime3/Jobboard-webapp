from django.urls import path

from . import views

urlpatterns = [
    #path('', views.get_peoples, name='all'),
    path('create', views.create, name='create'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('<str:token>', views.get_people_by_token, name='token'),
]

