from django.contrib import admin
from .models import Supplier, Shipper, Customer, UserProfile


admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Shipper)
admin.site.register(UserProfile)
