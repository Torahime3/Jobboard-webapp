from django.urls import path
from . import views


urlpatterns = [
      path('', views.getAllDatas, name='index'),
      path('<int:id>', views.get_JobAdvertisementsById, name='getId')

]
