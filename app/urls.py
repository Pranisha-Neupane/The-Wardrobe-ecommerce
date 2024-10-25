# myapp/urls.py

from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('', views.index, name='index'),  
    path('female_wear/', views.female_wear, name='female_wear'),
    path('male_wear/', views.male_wear, name='male_wear'),
    
]
