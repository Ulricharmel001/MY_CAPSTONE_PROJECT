from django.db import models
from inventory.models import Product, Customer

# ----------------------
# SalesOrder: Overall sales order
# ----------------------
class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sales_orders")
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"


# ----------------------
# SalesItem: Individual product sold
# ----------------------
class SalesItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales_items")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
