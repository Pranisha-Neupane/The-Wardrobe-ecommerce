
# views.py to filter the male and female clothes 
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



# code for search 
def search_clothes(request):
    query = request.GET.get('q')  # Get the search query from the request
    category = request.GET.get('category')  # Get the selected category if applicable
    clothes = Clothes.objects.all()

    if query:
        clothes = clothes.filter(name__icontains=query)  # Filter by name

    if category:
        clothes = clothes.filter(item_category=category)  # Filter by category

    return render(request, 'search_results.html', {'clothes': clothes, 'query': query, 'category': category})