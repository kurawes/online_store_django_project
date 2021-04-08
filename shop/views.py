from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

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


def category_delete_view(request, primary_key):
    # dictionary for initial data, field names as keys
    context = {}
    # fetch the object with the passed primary_key
    obj = get_object_or_404(Category, id=primary_key)

    if request.method == "POST":
        # delete the object
        obj.delete()
        # redirect back to previous page
        return reverse_lazy('category_list.html')

    return render(request, 'category_delete.html', context)
