



# cart_app/views.py
from django.shortcuts import redirect , render
from .models import CartItem
from app.models import Clothes
from django.contrib.auth.decorators import login_required
# from .models import CartItem

@login_required
def add_to_cart(request, product_id):
    product = Clothes.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        product=product, user=request.user,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart_app/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

