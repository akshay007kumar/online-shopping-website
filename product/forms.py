from django import forms
from . models import Product, Category, SubCategory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
