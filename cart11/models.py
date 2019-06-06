from django.db import models
from product.models import Product
from user.models import Customer


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, null=True, blank=True)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    timastamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s\'s Cart" % self.user.username


