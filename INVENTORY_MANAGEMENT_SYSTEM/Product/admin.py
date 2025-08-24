from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'created_at')
    search_fields = ('name', 'email', 'phone')
