from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Supplier, Customer, Store, Product

# Show products under each category
class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'supplier', 'unit_price', 'selling_price', 'reorder_level', 'is_active')
    list_filter = ('category', 'supplier', 'is_active')
    search_fields = ('name', 'sku', 'barcode')
