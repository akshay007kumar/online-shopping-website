from django.shortcuts import render, HttpResponse, redirect

from .models import Cart
from user.models import Customer, UserProfile
from product.models import Product


def mycart(request):
    myuser = Customer.objects.get(username=request.session['username'])
    mycart = Cart.objects.get(user=myuser.id)

    new_total = 0.00
    for product in mycart.product.all():
        price = (product.unit_price*(100-product.discount))/100
        new_total += price
        mycart.total = new_total
        mycart.save()

    context = {
        'profile': request.session['username'],
        'mycart': mycart,
        'cart_no': len(mycart.product.all()),
        'user': myuser,

    }
    return render(request, 'cart/mycart.htm', context)


def add(request, id):
    user = request.session.get('username', None)
    if user is None:
        print('Cart not available..')
        return redirect('products-page')

    myuser = Customer.objects.get(username=request.session['username'])
    try:
        mycart = Cart.objects.get(user=myuser.id)
        mycart.product.add(Product.objects.get(pk=id))
    except:
        mycart = Cart.objects.create(user=myuser,)
        mycart.product.add(Product.objects.get(pk=id))
        mycart.save()

    return redirect('cart')


def remove(request, id):
    myuser = Customer.objects.get(username=request.session['username'])
    mycart = Cart.objects.get(user=myuser.id)
    product = Product.objects.get(pk=id)
    if product in mycart.product.all():
        mycart.product.remove(product)
    else:
        print('product not available')

    return redirect('cart')
