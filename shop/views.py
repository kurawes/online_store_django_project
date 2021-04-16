from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Product, ProductType, Category


# in reference video home.html
def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})


# to see all the categories everywhere, add to settings.py TEMPLATES
def categories(request):
    return {"categories": Category.objects.all()}


# to see all the product types everywhere, add to settings.py TEMPLATES
def product_types(request):
    return {"product_types": ProductType.objects.all()}


def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'product_info.html', {"product": product})


def pt_list(request, product_type_slug):
    product_type = get_object_or_404(ProductType, slug=product_type_slug)
    products = Product.objects.filter(product_type=product_type)
    return render(request, 'pt_list.html', {'product_type': product_type, 'products': products})


# this gives some error message - The QuerySet value for an exact lookup must be limited to one result using slicing.
def cat_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product_type = ProductType.objects.filter(category=category)
    products = Product.objects.filter(product_type=product_type)
    return render(request, 'cat_list.html', {'category': category, 'product_type': product_type, 'products': products})


# ----------------------------------------------------
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


def product_view(request):
    context = {"products": Product.objects.all()}
    return render(request, 'product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)
        return render(request, 'search_results.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'search_results.html', {})

