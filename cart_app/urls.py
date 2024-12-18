
from django.urls import path
from . import views

urlpatterns = [
     path('', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Add item to cart
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),  # Remove item from cart
]
