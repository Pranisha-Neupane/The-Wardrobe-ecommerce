
# # Create your views here.
# from django.shortcuts import render
# # from .models import Product

# # def index(request):
# #     # products = Product.objects.all()
# #     return render(request, 'index.html')


# # recently changed code
# from .models import Clothing
# # from .models import Clothes 

# def index(request):
#     # Get all clothes for the home page
#     clothes = Clothing.objects.all()
#     return render(request, 'index.html', {'clothes': clothes})

# def female_wear(request):
#     # Filter clothes for females
#     female_clothes = Clothing.objects.filter(category='female')
#     return render(request, 'female_wear.html', {'clothes': female_clothes})

# def male_wear(request):
#     # Filter clothes for males
#     male_clothes = Clothing.objects.filter(category='male')
#     return render(request, 'male_wear.html', {'clothes': male_clothes})

from django.shortcuts import render
from .models import Clothes  

def index(request):
    # Get all clothes for the home page
    clothes = Clothes.objects.all()
    return render(request, 'index.html', {'clothes': clothes})

def female_wear(request):
    # Filter clothes for females
    female_clothes = Clothes.objects.filter(gender_category='female')
    return render(request, 'female_wear.html', {'clothes': female_clothes})

def male_wear(request):
    # Filter clothes for males
    male_clothes = Clothes.objects.filter(gender_category='male')
    return render(request, 'male_wear.html', {'clothes': male_clothes})
