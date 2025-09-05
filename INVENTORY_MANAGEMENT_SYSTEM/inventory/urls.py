# from django.urls import path
# from . import views

# urlpatterns = [
#     # Stores
#     path('stores/', views.store_list, name='store-list'),
#     path('stores/<int:pk>/', views.store_detail, name='store-detail'),
#     path('stores/<int:pk>/delete/', views.store_delete, name='store-delete'),

#     # Categories
#     path('categories/', views.category_list, name='category_list'),
#     path('categories/<int:pk>/', views.category_detail, name='category_detail'),
#     path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

#     # Products
#     path('products/', views.product_list, name='product_list'),
#     path('products/<int:pk>/', views.product_detail, name='product-detail'),
#     path('products/<int:pk>/delete/', views.product_delete, name='product-delete'),
#     path('products/<int:pk>/', views.product_detail, name='product-detail'), 

#     # Customers
#     path('customers/', views.customer_list, name='customer-list'),
#     path('customers/<int:pk>/', views.customer_detail, name='customer-detail'),
#     path('customers/<int:pk>/delete/', views.customer_delete, name='customer-delete'),

#     # Suppliers
#     path('suppliers/', views.supplier_list, name='supplier-list'),
#     path('suppliers/<int:pk>/', views.supplier_detail, name='supplier-detail'),
#     path('suppliers/<int:pk>/delete/', views.supplier_delete, name='supplier-delete'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path("products/", views.product_list, name="product_list"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"), 
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
    
    path("stores/", views.store_list, name="store-list"),
    path("stores/<int:pk>/", views.store_detail, name="store-detail"),
    path("stores/<int:pk>/delete/", views.store_delete, name="store-delete"),

    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:pk>/", views.category_detail, name="category_detail"),
    path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),

    path("suppliers/", views.supplier_list, name="supplier-list"),
    path("suppliers/<int:pk>/", views.supplier_detail, name="supplier-detail"),
    path("suppliers/<int:pk>/delete/", views.supplier_delete, name="supplier-delete"),

    path("customers/", views.customer_list, name="customer-list"),
    path("customers/<int:pk>/", views.customer_detail, name="customer-detail"),
    path("customers/<int:pk>/delete/", views.customer_delete, name="customer-delete"),
]