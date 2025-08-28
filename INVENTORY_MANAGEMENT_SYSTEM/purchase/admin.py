from django.contrib import admin
from .models import PurchaseOrder, PurchaseItem

# Register your models here.


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'date', 'total_amount')
  

@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('quantity',)
    

