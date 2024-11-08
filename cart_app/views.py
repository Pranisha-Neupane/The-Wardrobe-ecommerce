

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import CartItem
# from app.models import Clothes  # Assuming Clothes is your product model
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# # Add item to cart
# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Clothes, id=product_id)  # Get the product by its ID
#     quantity = int(request.POST.get('quantity', 1))  # Default quantity is 1

#     # Check if cart item already exists for this user and product
#     cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)

#     if not created:
#         cart_item.quantity += quantity  # If item already in cart, increase quantity
#         cart_item.save()

#     return redirect('cart')  # Redirect to cart page after adding

# # View for cart
# # @login_required
# # def cart_view(request):
# #     cart_items = CartItem.objects.filter(user=request.user)  # Get all cart items for the current user
# #     total_price = sum(item.get_total_price() for item in cart_items)  # Calculate total price

# #     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})



# @login_required
# def cart_view(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     total_price = sum(item.get_total_price() for item in cart_items)
#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})




# # Remove item from cart
# @login_required
# def remove_from_cart(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)  # Get the cart item
#     cart_item.delete()  # Remove the cart item

#     return redirect('cart')  # Redirect to the cart page after removal


from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from app.models import Clothes  # Assuming Clothes is your product model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Add item to cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Clothes, id=product_id)  # Get the product by its ID
    quantity = int(request.POST.get('quantity', 1))  # Default quantity is 1

    # Check if cart item already exists for this user and product
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    if created:
        cart_item.quantity = quantity  # Set initial quantity if item is new
    else:
        cart_item.quantity += quantity  # Increase quantity if item already in cart
    
    cart_item.save()  # Save changes

    return redirect('cart')  # Redirect to cart page after adding

# View for cart
@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)  # Get all cart items for the current user
    total_price = sum(item.get_total_price() for item in cart_items)  # Calculate total price

    # Debugging: Print cart items to check if they are retrieved correctly
    print("Cart items:", cart_items)
    for item in cart_items:
        print(f"Item: {item.product.name}, Quantity: {item.quantity}, Total Price: {item.get_total_price}")

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

# Remove item from cart
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)  # Get the cart item
    cart_item.delete()  # Remove the cart item

    return redirect('cart')  # Redirect to the cart page after removal
