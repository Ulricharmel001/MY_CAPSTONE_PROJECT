from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Store, Category, Supplier, Customer, Product
from .serializers import StoreSerializer, CategorySerializer, SupplierSerializer, CustomerSerializer, ProductSerializer


# ----------------------
# Store ViewSet
# ----------------------
class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


# ----------------------
# Category ViewSet
# ----------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ----------------------
# Supplier ViewSet
# ----------------------
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


# ----------------------
# Customer ViewSet
# ----------------------
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# ----------------------
# Product ViewSet
# ----------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
