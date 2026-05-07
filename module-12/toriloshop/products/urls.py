from django.urls import path
from . import views  #'.' means import from the current app package

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
]
