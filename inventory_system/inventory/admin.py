from django.contrib import admin
from .models import Product, InventorySale, UserProfile
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'order_date')  # Fields to show in the list view
    search_fields = ('product__name',)  # Search by product name
    list_filter = ('order_date',)  # Allows filtering by order date


admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(InventorySale)
