from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('group<int:pk>/', views.group, name='group'),
    path('description<int:pk>/', views.description, name='description'),
    path('', views.category_name, name='list'),
]
