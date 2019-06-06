from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_summary, name='order-summary'),
    path('payment/', views.payment, name='payment'),
]
