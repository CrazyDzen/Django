from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.category_name, name='list'),
]
