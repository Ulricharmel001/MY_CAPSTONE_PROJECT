
# Create your views here.
from django.shortcuts import render, redirect
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from inventory.models import Store, Category, Product, Customer
from stock.models import PurchaseOrder, SalesOrder
from django.contrib.auth.decorators import login_required


def welcome_view(request):
    """Landing page for new/unauthenticated users"""
    if request.user.is_authenticated:
        return redirect('dashboard_view')
    return render(request, 'dashboard/welcome.html')
@login_required
def dashboard_view(request):
    """Main dashboard with metrics for current user only"""
    store_count = Store.objects.filter(user=request.user).count()
    category_count = Category.objects.filter(user=request.user).count()
    product_count = Product.objects.filter(user=request.user).count()
    customer_count = Customer.objects.filter(user=request.user).count()
    purchase_qs = PurchaseOrder.objects.filter(user=request.user)
    sales_qs = SalesOrder.objects.filter(user=request.user)

    purchase_count = purchase_qs.count()
    sales_count = sales_qs.count()

    total_purchased = purchase_qs.aggregate(total=Sum('quantity'))['total'] or 0
    total_sold = sales_qs.aggregate(total=Sum('quantity'))['total'] or 0

    total_purchase_value = purchase_qs.aggregate(
        total=Sum(ExpressionWrapper(F('quantity') * F('unit_price'), output_field=DecimalField()))
    )['total'] or 0

    total_sales_value = sales_qs.aggregate(
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

