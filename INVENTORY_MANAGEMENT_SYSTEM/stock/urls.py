# stock/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Stock CRUD
    path("", views.stock_dashboard, name="stock_dashboard"),
    path("add/", views.add_stock, name="add_stock"),
    path("update/<int:pk>/", views.update_stock, name="update_stock"),
    path("delete/<int:pk>/", views.delete_stock, name="delete_stock"),

    # StockTransaction CRUD
    path("transactions/", views.transaction_list, name="transaction_list"),
    path("transactions/add/", views.transaction_add, name="transaction_add"),
    path("transactions/update/<int:pk>/", views.update_transaction, name="update_transaction"),
    path("transactions/delete/<int:pk>/", views.delete_transaction, name="transaction_delete"),
]
