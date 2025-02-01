from django import forms
from .models import Product, Sale
from .models import Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'price']


class UserCreationForm:
    pass


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'customer_name']

    def clean_quantity_sold(self):
        quantity_sold = self.cleaned_data['quantity_sold']
        product = self.instance.product
        if quantity_sold > product.quantity:
            raise forms.ValidationError(f"Not enough stock for {product.name}. Available: {product.quantity}")
        return quantity_sold


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']  # Only include fields that the user should fill

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than 0.")
        return quantity
