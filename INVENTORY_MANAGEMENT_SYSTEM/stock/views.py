from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock, StockTransaction, Store
from .forms import StockForm, StockTransactionForm

# ---------- Stock Dashboard ----------
def stock_dashboard(request):
    # Get all stores with related stocks and products
    stores = Store.objects.prefetch_related('stocks__product').all()

    context = {
        'stores': stores,
    }
    return render(request, 'stock/dashboard.html', context)

# ---------- Stock CRUD ----------
def add_stock(request):
    form = StockForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('stock_dashboard')
    return render(request, 'stock/add_stock.html', {'form': form})

def update_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    form = StockForm(request.POST or None, instance=stock)
    if form.is_valid():
        form.save()
        return redirect('stock_dashboard')
    return render(request, 'stock/add_stock.html', {'form': form, 'update': True})

def delete_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock_dashboard')
    return render(request, 'stock/delete_confirm.html', {'object': stock})

# ---------- StockTransaction CRUD ----------
def transaction_list(request):
    transactions = StockTransaction.objects.select_related('product', 'store').all()
    return render(request, 'stock/transaction_list.html', {'transactions': transactions})

def transaction_add(request):
    form = StockTransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('transaction_list')
    return render(request, 'stock/transaction_add.html', {'form': form})

def update_transaction(request, pk):
    transaction = get_object_or_404(StockTransaction, pk=pk)
    form = StockTransactionForm(request.POST or None, instance=transaction)
    if form.is_valid():
        form.save()
        return redirect('transaction_list')
    return render(request, 'stock/transaction_add.html', {'form': form, 'update': True})

def delete_transaction(request, pk):
    transaction = get_object_or_404(StockTransaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'stock/delete_confirm.html', {'object': transaction})
