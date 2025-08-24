from rest_framework import serializers
from .models import PurchaseOrder, PurchaseItem
from inventory.serializers import SupplierSerializer, ProductSerializer

# Single product in purchase order
class PurchaseItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = PurchaseItem
        fields = "__all__"

# Purchase order with items
class PurchaseOrderSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    items = PurchaseItemSerializer(many=True, read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = "__all__"
