# custom_context.py
from .models import CartItem

def cart_item_count(request):
    cart_count = CartItem.objects.count()
    return {'cart_count': cart_count}
# 