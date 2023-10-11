from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_peoples, name='all'),
    path('<int:id>', views.get_people_by_id, name='id')
]
