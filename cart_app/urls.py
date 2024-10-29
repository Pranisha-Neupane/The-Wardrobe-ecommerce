

# cart_app/urls.py
from django.urls import path
from . import views

# urlpatterns = [
#     #  path('cart/', views.cart_view, name='cart'), 
#     path('', views.cart_view, name='cart'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    
# ]


urlpatterns = [
    path('', views.cart_view, name='cart'), 
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart-item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),  # For updating item quantities
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),  # For removing items
]
