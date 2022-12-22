from django.urls import path
from . import  views
app_name='plantnurseryapp'

urlpatterns = [
    path('', views.home,name='home'),
    path('add/', views.add, name='add'),
    path('plant/<int:plant_id>/', views.detail, name='detail'),
    path('update/<int:plant_id>/',views.update, name='update'),
    path('delete/<int:plant_id>/', views.delete, name='delete'),
]