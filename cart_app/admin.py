# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'get_total_price')
    search_fields = ('product__name', 'user__username')  # Allows searching by product name and username
    list_filter = ('user',)  # Filter cart items by user
    readonly_fields = ('get_total_price',)  # Make total price read-only in admin

admin.site.register(CartItem, CartItemAdmin)
