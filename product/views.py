from django.shortcuts import render
from django.db.models import Q

from .models import Product
from user.models import Customer
from cart11.models import Cart


def show_products(request):
    cart_no = None
    myuser = None
    # for cart items badge
    if request.session.get('username', None):
        if not None:
            myuser = Customer.objects.get(username=request.session['username'])
            try:
                mycart = Cart.objects.get(user=myuser.id)
            except:
                mycart = Cart.objects.create(user=myuser,)
            cart_no = len(mycart.product.all())
    products = Product.objects.all()
    if request.method == "POST":
        if 'btnSearch' in request.POST.keys():
            txtSearch = request.POST['txtSearch']
            print('Searching: ', txtSearch)
            products = Product.objects.filter(
                Q(product_name__icontains=txtSearch)).distinct()

    context = {
        'products': products,
        'profile': request.session.get('username'),
        'cart_no': cart_no,
        'user': myuser,
    }

    return render(request, 'product/index.htm', context)


def product_details(request, id):
    cart_no = None
    myuser = None
    # for cart items badge
    if request.session.get('username', None):
        if not None:
            myuser = Customer.objects.get(username=request.session['username'])
            try:
                mycart = Cart.objects.get(user=myuser.id)
            except:
                mycart = Cart.objects.create(user=myuser,)
            cart_no = len(mycart.product.all())

    product = Product.objects.get(pk=id)
    context = {
        'product': product,
        'profile': request.session.get('username'),
        'cart_no': cart_no,
        'user': myuser,
    }
    return render(request, 'product/details.htm', context)
