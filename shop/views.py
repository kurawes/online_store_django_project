from django.shortcuts import render
from .models import Product, ProductType, Category


def home_page_view(request):
    return render(request, 'home.html')


def about_page_view(request):
    return render(request, 'about.html')


def contact_page_view(request):
    return render(request, 'contact.html')


def shop_view(request):
    # dictionary for data
    context = {"products": Product.objects.all()}
    return render(request, 'shop.html', context)


def category_view(request):
    context = {"categories": Category.objects.all()}
    return render(request, 'category_list.html', context)


def product_type_view(request):
    context = {"product_types": ProductType.objects.all()}
    return render(request, 'product_type_list.html', context)
