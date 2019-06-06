from django.db import models
from django.db.models.signals import post_save


class Customer(models.Model):
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    status = models.CharField(max_length=10, default='Active')

    def __str__(self):
        return self.username


class Shipper(models.Model):
    company_name = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    fullname = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    company_name = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name


class UserProfile(models.Model):
    first_name = models.CharField(max_length=12, default='First Name')
    last_name = models.CharField(max_length=12, default='Last Name')
    permanent_address = models.TextField(default='Permanent Address')
    shipping_address = models.TextField(default='Shipping Address')
    profile_image = models.ImageField(
        default='default.png', upload_to='profile')
    bio = models.TextField(default='Your Bio')
    joined = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(default='1990-01-01')
    profile_status = models.CharField(max_length=20, verbose_name='Activate')

    user = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


def create_user_profile(sender, instance, created, **kwargs):
    print("Sender:", sender)
    print("Instance:", instance, type(instance))
    print("Created:", created)
    print("kwargs:", kwargs)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=Customer)
