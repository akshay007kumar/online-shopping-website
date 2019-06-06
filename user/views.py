from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import logout

from .forms import CustomerForm, LoginForm, ChangePassword, UserProfileForm
from .models import Customer, UserProfile
from product.models import Product


def testing_index(request):
    return redirect('products-page')
    context = {}
    return render(request, 'test/testingIndex.htm', context)


def index(request):
    user = Customer.objects.all()
    context = {
        'users': user
    }
    return render(request, 'user/index.html', context)


def login(request):
    products = Product.objects.all()
    if request.session.get('username'):
        return redirect('products-page')

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        username = request.POST['username']
        password = request.POST['password']
        auth_user = Customer.objects.filter(
            username=username, password=password)

        if auth_user.exists():
            print('login success!')
            request.session['username'] = username

            return redirect('products-page')
        else:
            messages.info(request, 'invalid username or password')

    context = {
        'form': form,

    }
    return render(request, 'user/login.htm', context)


def user_logout(request):
    # request.session['username'] = None
    logout(request)

    return redirect('products-page')


def signup(request):
    form = CustomerForm()
    if request.method == 'POST':
        username = request.POST['username']
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            print('User registered successfully!')
            request.session['username'] = username
            return redirect('products-page')

    context = {
        'form': form,
        'caption': 'Registration',
    }
    return render(request, 'user/signup.htm', context)


def user_profile(request, id):
    myuser = Customer.objects.get(username=request.session['username'])
    user = UserProfile.objects.get(pk=id)
    form = UserProfileForm(request.POST or None, instance=user)
    print(user.first_name)
    if request.method == "POST":
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'user1': user,
        'user': myuser,
        'profile': request.session.get('username'),
    }
    return render(request, 'user/profile.htm', context)


# not working
def change_password(request, id):
    form = ChangePassword()
    if request.method == 'POST':
        form = ChangePassword(request.POST or None)
        user = Customer.objects.get(pk=id)

        newPassword = request.POST['newPassword']
        repeatPassword = request.POST['repeatPassword']
        if newPassword == repeatPassword:
            user.password = newPassword
            print('password updated!')
        else:
            print('password doesnot match!')

    context = {
        'form': form
    }

    return render(request, 'user/update_password.htm', context)
