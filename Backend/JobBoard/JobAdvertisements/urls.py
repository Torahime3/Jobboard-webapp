from django.urls import path
from . import views


urlpatterns = [
      path('', views.getAllDatas, name='index'),
      path('<int:id>', views.get_JobAdvertisementsById, name='getId'),
      path('<str:token>/all', views.getAll, name='getAll'),
      path('<str:token>/create', views.create, name='create'),
      path('<str:token>/update', views.update, name='update'),
      # path('<str:token>/delete', views.delete, name='delete'),
]
