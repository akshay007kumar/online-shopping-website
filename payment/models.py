from django.db import models

from user.models import Shipper, Customer

class Order(models.Model):
    order_date = models.DateTimeField()
    order_number = models.IntegerField(unique=True)

    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_date
