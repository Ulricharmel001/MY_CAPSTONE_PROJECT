from django.urls import path
from . import views

# URL patterns for normal Django views (not using DRF routers)
urlpatterns = [
    # Store endpoints
    path('stores/', views.store_list, name='store_list'),          # GET all stores, POST new store
    path('stores/<int:pk>/', views.store_detail, name='store_detail'),  # GET, PUT, DELETE a single store

    # Category endpoints
    path('categories/', views.category_list, name='category_list'), 
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),

    # Supplier endpoints
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/<int:pk>/', views.supplier_detail, name='supplier_detail'),

    # Customer endpoints
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),

    # Product endpoints
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]
