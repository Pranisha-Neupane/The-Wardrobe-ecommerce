



# cart_app/views.py
from django.shortcuts import  render
from .models import CartItem
from app.models import Clothes
from django.contrib.auth.decorators import login_required
# from .models import CartItem


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })




# recently added
from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404, redirect

# from .models import Clothes, CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Clothes, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        product=product, user=request.user,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # Get updated cart item count
    cart_item_count = CartItem.objects.filter(user=request.user).count()

    return JsonResponse({'cartItemCount': cart_item_count})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')



@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart')


# from django.http import JsonResponse
# from .models import CartItem, Clothes