from rest_framework import generics
from .models import Stock, StockTransaction
from .serializers import StockSerializer, StockTransactionSerializer

# ----------------------
# Stock Views
# ----------------------
class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


# ----------------------
# StockTransaction Views
# ----------------------
class StockTransactionListCreateView(generics.ListCreateAPIView):
    queryset = StockTransaction.objects.all()
    serializer_class = StockTransactionSerializer


class StockTransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockTransaction.objects.all()
    serializer_class = StockTransactionSerializer
