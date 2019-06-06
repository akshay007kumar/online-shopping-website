from django.shortcuts import render

from user.models import UserProfile, Customer
from cart11.models import Cart


def order_summary(request):
    myuser = Customer.objects.get(username=request.session['username'])
    mycart = Cart.objects.get(user=myuser.id)
    profile = UserProfile.objects.get(user=myuser.id)
    context = {
        'address': profile.shipping_address,
        'profile': request.session['username'],
        'mycart': mycart,
        'cart_no': len(mycart.product.all()),
        'user': myuser,
    }
    return render(request, 'payment/order.htm', context)


def payment(request):

    context = {

    }
    return render(request, 'payment/payment.htm', context)
