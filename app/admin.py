
from django.contrib import admin
from .models import Clothes

admin.site.register(Clothes)



# for sorting the clothes new code
# admin.py

# @admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'gender_category', 'item_category')
    list_filter = ('gender_category', 'item_category')
    search_fields = ('name',)
