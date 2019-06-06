from django.urls import path
from . import views

urlpatterns = [
    path('', views.mycart, name='cart'),
    path('add/<int:id>/', views.add, name="add-to-cart"),
    path('remove/<int:id>/', views.remove, name="remove-from-cart"),
]
