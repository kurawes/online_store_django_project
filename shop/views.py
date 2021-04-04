from django.shortcuts import render
from .models import Product, ProductType, Category


def home_page_view(request):
    return render(request, 'home.html')


def about_page_view(request):
    return render(request, 'about.html')


def contact_page_view(request):
    return render(request, 'contact.html')


def shop_view(request):
    # dictionary for initial data
    context = {}

    # fill the dictionary during Internationalization
    context["products"] = Product.objects.all()
    return render(request, 'shop.html', context)
