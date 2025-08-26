from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SalesOrder, SalesItem
from inventory.models import Product, Customer
from .serializers import SalesOrderSerializer, SalesItemSerializer

# ----------------------
# SalesOrder API Views
# ----------------------

class SalesOrderListCreateView(APIView):
    """
    Handles listing all sales orders and creating a new sales order.
    GET: Return all sales orders in JSON.
    POST: Create a new sales order with provided data.
    """
    def get(self, request):
        orders = SalesOrder.objects.all()
        serializer = SalesOrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SalesOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save new sales order
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesOrderDetailView(APIView):
    """
    Handles retrieving, updating, or deleting a single sales order by ID.
    """
    def get_object(self, pk):
        return SalesOrder.objects.get(pk=pk)

    def get(self, request, pk):
        """Return a single sales order"""
        order = self.get_object(pk)
        serializer = SalesOrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update a single sales order"""
        order = self.get_object(pk)
        serializer = SalesOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a single sales order"""
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------
# SalesItem API Views
# ----------------------

class SalesItemListCreateView(APIView):
    """
    Handles listing all sales items and creating a new sales item.
    GET: Return all sales items in JSON.
    POST: Create a new sales item with provided data.
    """
    def get(self, request):
        items = SalesItem.objects.all()
        serializer = SalesItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SalesItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save new sales item
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesItemDetailView(APIView):
    """
    Handles retrieving, updating, or deleting a single sales item by ID.
    """
    def get_object(self, pk):
        return SalesItem.objects.get(pk=pk)

    def get(self, request, pk):
        """Return a single sales item"""
        item = self.get_object(pk)
        serializer = SalesItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update a single sales item"""
        item = self.get_object(pk)
        serializer = SalesItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a single sales item"""
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
