from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.get_peoples, name='all'),
    path('<int:people_id>',views.get_people_by_id, name='id')
]
