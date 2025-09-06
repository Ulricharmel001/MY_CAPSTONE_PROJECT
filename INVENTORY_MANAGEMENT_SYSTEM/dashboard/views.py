

# Create your views here.
from django.shortcuts import render, redirect
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from inventory.models import Store, Category, Product, Customer
from stock.models import PurchaseOrder, SalesOrder


def welcome_view(request):
    """Landing page for new/unauthenticated users"""
    if request.user.is_authenticated:
        return redirect('dashboard_view')
    return render(request, 'dashboard/welcome.html')

def dashboard_view(request):
    """Main dashboard with metrics"""
    store_count = Store.objects.count()
    category_count = Category.objects.count()
    product_count = Product.objects.count()
    customer_count = Customer.objects.count()
    purchase_count = PurchaseOrder.objects.count()
    sales_count = SalesOrder.objects.count()

    total_purchased = PurchaseOrder.objects.aggregate(total=Sum('quantity'))['total'] or 0
    total_sold = SalesOrder.objects.aggregate(total=Sum('quantity'))['total'] or 0

    total_purchase_value = PurchaseOrder.objects.aggregate(
        total=Sum(ExpressionWrapper(F('quantity') * F('unit_price'), output_field=DecimalField()))
    )['total'] or 0

    total_sales_value = SalesOrder.objects.aggregate(
        total=Sum(ExpressionWrapper(F('quantity') * F('unit_price'), output_field=DecimalField()))
    )['total'] or 0

    context = {
        'store_count': store_count,
        'category_count': category_count,
        'product_count': product_count,
        'customer_count': customer_count,
        'purchase_count': purchase_count,
        'sales_count': sales_count,
        'total_purchased': total_purchased,
        'total_sold': total_sold,
        'total_purchase_value': total_purchase_value,
        'total_sales_value': total_sales_value,
    }
    return render(request, 'dashboard/main.html', context)
