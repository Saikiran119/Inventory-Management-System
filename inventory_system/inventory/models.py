from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField(default='No description provided')
    low_stock_threshold = models.PositiveIntegerField(default=10)
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity})"

    def update_quantity(self, quantity_sold):
        if self.quantity >= quantity_sold:
            self.quantity -= quantity_sold
            self.save()
        else:
            raise ValueError("Not enough stock available.")


class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class InventorySale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255, default='Unknown')
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sale_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inventory_sale'  # Ensure that this matches the actual table name in the database

    def __str__(self):
        return f'Sale of {self.quantity} {self.product.name} to {self.customer_name} on {self.sale_date}'


# inventory/models.py

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255, default='Unknown')
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date = models.DateTimeField(auto_now_add=True)
    sale_type = models.CharField(max_length=50, default='regular')  # Optional field to differentiate sales types

    class Meta:
        db_table = 'sale'

    def update_inventory(self):
        # Decrease product quantity after sale
        self.product.quantity -= self.quantity
        self.product.save()

    def __str__(self):
        return f'Sale of {self.quantity} {self.product.name} to {self.customer_name}'


# Optional Order model for tracking orders
# models.py

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # Quantity cannot be null
    total_price = models.DecimalField(max_digits=10, null=True, decimal_places=2, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Override the save method to set the product name and calculate total price."""
        if self.product:
            self.product_name = self.product.name

        if self.product and self.quantity:
            # Calculate total price before saving the order
            self.total_price = self.product.price * self.quantity
        else:
            # If product or quantity is missing, set total_price to None or 0
            self.total_price = 0.00

        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.product.name}"

    def mark_as_success(self):
        """Mark the order as successful."""
        self.status = 'success'
        self.save()

    class Meta:
        db_table = 'inventory_order'
