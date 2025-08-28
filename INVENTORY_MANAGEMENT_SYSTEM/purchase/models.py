from django.db import models
from inventory.models import Supplier, Product

# ----------------------
# PurchaseOrder: Overall purchase
# ----------------------
class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('received', 'Received'),
        ('cancelled', 'Cancelled'),
    ]

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="purchase_orders")
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Purchase {self.id} - {self.supplier.name}"

# ----------------------
# PurchaseItem: Individual product in order
# ----------------------
class PurchaseItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cost_price = models.FloatField()

    def total_price(self):
        return self.quantity * self.cost_price

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
