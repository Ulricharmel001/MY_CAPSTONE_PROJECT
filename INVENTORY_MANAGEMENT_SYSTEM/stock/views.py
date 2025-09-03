from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PurchaseForm, SalesForm
from .models import PurchaseOrder, SalesOrder

# ------------------------
# CREATE PURCHASE ORDER
# ------------------------
def create_purchase(request):
    """
    Handles purchase creation.
    Adds purchased quantity to product stock automatically.
    """
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            
            # Add purchased quantity to stock
            purchase.product.stock += purchase.quantity
            purchase.product.save()

            messages.success(
                request,
                f"Purchase order for {purchase.quantity} {purchase.product.name} added."
            )
            return redirect("purchase_list")
    else:
        form = PurchaseForm()

    return render(request, "stock/create_purchase.html", {"form": form})


# ------------------------
# CREATE SALES ORDER
# ------------------------
def create_sale(request):
    """
    Handles sales creation.
    Deducts sold quantity from product stock.
    Prevents sale if not enough stock.
    """
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)

            # Stock check
            if sale.product.stock < sale.quantity:
                messages.error(
                    request,
                    f"Not enough stock for {sale.product.name}. Available: {sale.product.stock}"
                )
                return redirect("sale_list")

            # Deduct stock and save
            sale.product.stock -= sale.quantity
            sale.product.save()
            sale.save()

            messages.success(
                request,
                f"Sales order for {sale.quantity} {sale.product.name} processed."
            )
            return redirect("sale_list")
    else:
        form = SalesForm()

    return render(request, "stock/create_sale.html", {"form": form})


def purchase_list(request):
    """
    Display all purchase orders in a table.
    """
    purchases = PurchaseOrder.objects.all().order_by('-date')
    return render(request, "stock/purchase_list.html", {"purchases": purchases})

# ------------------------
# LIST SALES ORDERS
# ------------------------
def sale_list(request):
    """
    Display all sales orders in a table.
    """
    sales = SalesOrder.objects.all().order_by('-date')
    return render(request, "stock/sale_list.html", {"sales": sales})


