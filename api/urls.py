from django.urls import path, include
from api import  views


urlpatterns = [
 path('list/',views.list_clients, name = 'list_clients'),
 path('saving/', views.save_client, name='save_client'), 
 path('deleting/<int:id>/', views.delete_client, name='delete_client'),
 path('', views.home, name='home'),
]