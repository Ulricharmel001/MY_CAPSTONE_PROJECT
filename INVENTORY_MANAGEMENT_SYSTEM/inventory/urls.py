from django.urls import path
from .views import (
    StoreListView, StoreDetailView, StoreDeleteView,
    CategoryListView, CategoryDetailView, CategoryDeleteView,
    ProductListView, ProductDetailView, ProductDeleteView,
    CustomerListView, CustomerDetailView, CustomerDeleteView,
    SupplierListView, SupplierDetailView, SupplierDeleteView
)

urlpatterns = [
    # Stores
    path("stores/", StoreListView.as_view(), name="store-list"),
    path("stores/<int:pk>/", StoreDetailView.as_view(), name="store-detail"),
    path("stores/<int:pk>/delete/", StoreDeleteView.as_view(), name="store-delete"),

    # Categories
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),

    # Products
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),

    # Customers
    path("customers/", CustomerListView.as_view(), name="customer-list"),
    path("customers/<int:pk>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("customers/<int:pk>/delete/", CustomerDeleteView.as_view(), name="customer-delete"),

    # Suppliers
    path("suppliers/", SupplierListView.as_view(), name="supplier-list"),
    path("suppliers/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
    path("suppliers/<int:pk>/delete/", SupplierDeleteView.as_view(), name="supplier-delete"),
]
