from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' # অথবা আপনার প্রোডাক্টের নির্দিষ্ট ফিল্ডগুলো যেমন: ['name', 'price', 'quantity']
        
        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Product ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Product Name'}),
            'sku': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'SKU'}),
            'price': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Quantity'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Supplier'}),
        }