from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from .forms import PurchaseOrderForm, SalesOrderForm
from .models import PurchaseOrder, SalesOrder

# PURCHASE LIST : list all purchase items 
def purchase_list(request):
    purchases = PurchaseOrder.objects.all().order_by('-date')
    return render(request, "stock/purchase_list.html", {"purchases": purchases})

# CREATE PURCHASE: This provide a form to create  purchase
""" and also made a calcultion of adding purchase value to stock of product in product model , show 
quantity and name odf product  bought """
def create_purchase(request):
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                purchase = form.save()
                purchase.product.stock += purchase.quantity
                purchase.product.save()
                messages.success(request, f"{purchase.quantity} {purchase.product.name} purchased.")
                return redirect("purchase_list")
        # If form is invalid, re-render the form with errors
        return render(request, "stock/create_purchase.html", {"form": form})
    else:
        form = PurchaseOrderForm()
    return render(request, "stock/create_purchase.html", {"form": form})

# SALES LIST, list all sales items
def sale_list(request):
    sales = SalesOrder.objects.all().order_by('-date')
    return render(request, "stock/sale_list.html", {"sales": sales})

# CREATE SALE: this would make it possible to create sale transactions 
# it also check if sales quantity is positive and if its not, it would display 
# not enough message, and show available amount for user to know what amount sell
def create_sale(request):
    if request.method == "POST":
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            if sale.product.stock < sale.quantity:
                messages.error(request, f"Not enough stock for {sale.product.name}. Available: {sale.product.stock}")
                return render(request, "stock/create_sale.html", {"form": form})
            with transaction.atomic():
                sale.product.stock -= sale.quantity
                sale.product.save()
                sale.save()
                messages.success(request, f"{sale.quantity} {sale.product.name} sold.")
                return redirect("sale_list")
        # If form is invalid, re-render the form with errors
        return render(request, "stock/create_sale.html", {"form": form})
    else:
        form = SalesOrderForm()
    return render(request, "stock/create_sale.html", {"form": form})





