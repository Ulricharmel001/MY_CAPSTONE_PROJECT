from rest_framework import serializers
from .models import Stock, StockTransaction
from inventory.serializers import ProductSerializer, StoreSerializer

# Quantity per product per store
class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    store = StoreSerializer(read_only=True)

    class Meta:
        model = Stock
        fields = "__all__"

# Stock movements (in/out)
class StockTransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    store = StoreSerializer(read_only=True)

    class Meta:
        model = StockTransaction
        fields = "__all__"
