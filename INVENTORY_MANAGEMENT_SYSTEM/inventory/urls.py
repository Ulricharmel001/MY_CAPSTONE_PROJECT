# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ----------------------
    # Store URLs
    # ----------------------
    path('stores/', views.store_list, name='store-list'),
    path('stores/<int:pk>/', views.store_detail, name='store-detail'),

    # ----------------------
    # Category URLs
    # ----------------------
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    # ----------------------
    # Delete URLs
    # ----------------------
    path('stores/<int:pk>/delete/', views.store_delete, name='store-delete'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category-delete'),

    # product
    path("products/", views.product_list, name="product_list"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
    

]
