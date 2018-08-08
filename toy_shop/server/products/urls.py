from django.urls import path
from . import views
from . import endpoints

app_name = 'products'


endpoints = [
    path('api/', endpoints.api_product_list, name='api_list')
]


urlpatterns = [
    path('group<int:pk>/', views.category_list, name='group'),
    path('good<int:pk>/', views.description, name='description'),
    path('toys/', views.toys, name='toys'),
    path('product/', views.ProductList.as_view(), name='product'),
    path('edit/', views.ProductCreate.as_view(), name='edit'),
    path('update<int:pk>/', views.ProductsUpdate.as_view(), name='update'),
    path('delete<int:pk>/', views.ProductsDelete.as_view(), name='delete'),
    #path('', views.products_list, name='list'),
] + endpoints
