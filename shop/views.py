from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView

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


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_edit.html'
    context_object_name = 'category'
    fields = '__all__'
    success_url = reverse_lazy('category_list')


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_create.html'
    fields = '__all__'
    success_url = reverse_lazy('category_list')


def product_type_view(request):
    context = {"product_types": ProductType.objects.all()}
    return render(request, 'product_type_list.html', context)


class PTDeleteView(DeleteView):
    model = ProductType
    template_name = 'product_type_delete.html'
    context_object_name = 'product_type'
    success_url = reverse_lazy('product_type_list')


class PTUpdateView(UpdateView):
    model = ProductType
    template_name = 'product_type_edit.html'
    context_object_name = 'product_type'
    fields = '__all__'
    success_url = reverse_lazy('product_type_list')


class PTCreateView(CreateView):
    model = ProductType
    template_name = 'product_type_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_type_list')


def product_view(request):
    context = {"products": Product.objects.all()}
    return render(request, 'product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_edit.html'
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')
