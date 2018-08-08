from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'securities'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', auth_views.logout, {'next_page': 'categories:list'}, name='logout'),
    path('', views.LoginView.as_view(), name='login')
]