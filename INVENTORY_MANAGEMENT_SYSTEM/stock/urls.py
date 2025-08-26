from django.urls import path
from .views import (
    StockListCreateView, StockDetailView,
    StockTransactionListCreateView, StockTransactionDetailView
)

urlpatterns = [
    # Stock endpoints
    path('stock/', StockListCreateView.as_view(), name='stock-list'),
    path('stock/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),

    # StockTransaction endpoints
    path('stock-transactions/', StockTransactionListCreateView.as_view(), name='transaction-list'),
    path('stock-transactions/<int:pk>/', StockTransactionDetailView.as_view(), name='transaction-detail'),
]
