from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import PurchaseOrder, PurchaseItem
from .serializers import PurchaseOrderSerializer, PurchaseItemSerializer

# ----------------------
# PurchaseOrder Views
# ----------------------

# List all purchase orders or create a new one
class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all().order_by('-date')
    serializer_class = PurchaseOrderSerializer

# Retrieve, update, or delete a single purchase order
class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

# ----------------------
# PurchaseItem Views
# ----------------------

# List all purchase items or create a new one
class PurchaseItemListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer

# Retrieve, update, or delete a single purchase item
class PurchaseItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer
