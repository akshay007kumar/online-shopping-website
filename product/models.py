from django.db import models
from user.models import Shipper, Supplier, Customer


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=40)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_desctiption = models.TextField()
    quantity_per_unit = models.IntegerField()
    unit_price = models.IntegerField()
    discount = models.IntegerField()
    picture = models.ImageField(upload_to='product/', default='default.png')

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # slug =

    def __str__(self):
        return self.product_name


