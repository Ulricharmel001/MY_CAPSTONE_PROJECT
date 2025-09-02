from rest_framework import serializers
from .models import PurchaseOrder, SalesOrder

# ------------------------
# Purchase Serializer
# ------------------------
class PurchaseSerializer(serializers.ModelSerializer):
    """
    Serializer to convert PurchaseOrder objects
    into JSON for API responses and validate incoming data.
    """
    class Meta:
        model = PurchaseOrder
        fields = ["id", "product", "store", "quantity", "unit_price", "date"]


# ------------------------
# Sales Serializer
# ------------------------
class SalesSerializer(serializers.ModelSerializer):
    """
    Serializer to convert SalesOrder objects
    into JSON for API responses and validate incoming data.
    """
    class Meta:
        model = SalesOrder
        fields = ["id", "product", "store", "quantity", "unit_price", "date"]
