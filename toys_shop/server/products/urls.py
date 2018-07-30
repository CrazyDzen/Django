from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group<int:pk>/', views.category_list, name='group'),
    path('good<int:pk>/', views.description, name='description'),
    path('toys/', views.toys, name='toys'),
    path('admin/', views.admin, name='admin'),
    path('edit/', views., name='edit')
]
