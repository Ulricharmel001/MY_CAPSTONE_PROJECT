from rest_framework import serializers
from .models import PurchaseOrder, PurchaseItem
from inventory.models import Supplier, Product

# Single product in purchase order
class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = ['product', 'quantity', 'cost_price']  # only input fields

# Purchase order with items
class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseItemSerializer(many=True)  # allow input of items

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'supplier', 'date', 'total_amount', 'items']

    # Create PurchaseOrder along with nested PurchaseItems
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        purchase_order = PurchaseOrder.objects.create(**validated_data)
        total_amount = 0

        for item_data in items_data:
            item = PurchaseItem.objects.create(purchase_order=purchase_order, **item_data)
            total_amount += item.quantity * item.cost_price

        purchase_order.total_amount = total_amount
        purchase_order.save()
        return purchase_order
