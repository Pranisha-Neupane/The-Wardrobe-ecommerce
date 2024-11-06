
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


# views.py
# from django.shortcuts import render
# from .models import Clothes

def search_items(request):
    query = request.GET.get('q')
    items = Clothes.objects.all()
    
    if query:
        items = items.filter(item_category__icontains=query)

    return render(request, 'search.html', {'items': items, 'query': query})






# for sorting the clothes new code

def product_list(request):
    sort_by = request.GET.get('sort', 'name_asc')  # Default to sorting by name A-Z

    if sort_by == 'name_asc':
        clothes = Clothes.objects.all().order_by('name')  # A-Z
    elif sort_by == 'name_desc':
        clothes = Clothes.objects.all().order_by('-name')  # Z-A
    elif sort_by == 'price_asc':
        clothes = Clothes.objects.all().order_by('price')  # Low to high
    elif sort_by == 'price_desc':
        clothes = Clothes.objects.all().order_by('-price')  # High to low
    else:
        clothes = Clothes.objects.all()  # Default

    return render(request, 'index.html', {'clothes': clothes, 'sort_by': sort_by})
