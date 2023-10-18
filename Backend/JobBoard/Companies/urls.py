from django.urls import path
from . import views


urlpatterns = [
      path('<int:id>', views.getCompanyById, name='company'),
      path('<str:token>', views.getAll, name='companywithToken'),
      path('<str:token>/delete', views.delete, name='delete'),
      path('<str:token>/create', views.create, name='create'),
      path('<str:token>/update', views.update, name='update'),
]
