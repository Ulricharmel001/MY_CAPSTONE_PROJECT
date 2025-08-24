from django.db import models

# Create your models here.
from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)  # Supplier name
    email = models.EmailField(blank=True, null=True)  # Optional email
    phone = models.CharField(max_length=20, blank=True, null=True)  # Contact phone
    address = models.TextField(blank=True, null=True)  # Supplier address
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation date
    updated_at = models.DateTimeField(auto_now=True)  # Last updated

    def __str__(self):
        return self.name
