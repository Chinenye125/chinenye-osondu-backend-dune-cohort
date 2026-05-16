from django.urls import path 
from . import views  #'.' means import from the current app package
from .views import product_list_json, product_detail_json
from .views import ProductListAPIView, ProductDetailAPIView, CategoryListAPIView, ProductCreateAPIView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('products/', views.product_list, name = 'product_list'),
    path('about/', views.about, name ='about'),

    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/<str:slug>/', views.category_detail, name='category_detail'),

    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),  


    path('api/products/', views.ProductListAPIView.as_view(), name='product_list_api'),
    path('api/products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product_detail_api'),
    path('api/categories/', views.CategoryListAPIView.as_view(), name='category_list_api'),
    path('products/create/', views.ProductCreateAPIView.as_view(), name='product_create_api'),
    path('api/products/json/', views.product_list_json, name='product_list_json'),
    path('api/products/<int:pk>/json/', views.product_detail_json, name='product_detail_json'),

]
