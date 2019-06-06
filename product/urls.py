from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_products, name="products-page"),
    path('<int:id>/', views.product_details, name="product-detail"),
]
