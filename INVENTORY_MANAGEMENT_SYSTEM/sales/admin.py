from django.contrib import admin
from .models import SalesItem, SalesOrder
# Register your models here.

@admin.register(SalesItem)
class SalesItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price')  

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'total_amount')  