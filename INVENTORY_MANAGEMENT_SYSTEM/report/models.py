from django.db import models

# Create your models here.
from django.db import models
from inventory.models import Product, Store

# ----------------------
# Inventory Report Model
# ----------------------
class Report(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    report_file = models.FileField(upload_to="reports/")  # Exported report file

    def __str__(self):
        return self.title
