from django.urls import path
from . import views


app_name = 'securities'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', views.LoginView.as_view(), name='login')
]