from rest_framework import serializers
from .models import SalesOrder, SalesItem
from inventory.serializers import CustomerSerializer, ProductSerializer

# Single product sold
class SalesItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = SalesItem
        fields = "__all__"

# Sales order with items
class SalesOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    items = SalesItemSerializer(many=True, read_only=True)

    class Meta:
        model = SalesOrder
        fields = "__all__"
