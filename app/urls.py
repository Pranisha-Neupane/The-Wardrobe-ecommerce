# myapp/urls.py

from django.urls import path
from . import views  # Import views from your app
# from .views import search_clothes  #for searching the products based on category choices
from .views import search_items

urlpatterns = [
    path('', views.index, name='index'),  
    path('female_wear/', views.female_wear, name='female_wear'),
    path('male_wear/', views.male_wear, name='male_wear'),
    path('search/', search_items, name='search_items'),
    path('sort/', views.product_list, name='product_list'),

]
    
