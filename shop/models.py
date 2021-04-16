from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    # objects = models.Manager()

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse('shop:cat_list', args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name='product_type', on_delete=models.CASCADE)
    # objects = models.Manager()

    class Meta:
        verbose_name_plural = "product_types"

    def get_absolute_url(self):
        return reverse('shop:pt_list', args=[self.slug])

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(in_active=True)


class Product(models.Model):
    AVAILABLE = "Available"
    NOT_AVAILABLE = "Not Available"
    ARCHIVED = "Archived"
    OUT_OF_STOCK = "Out of stock"

    AVAILABILITY = [
        (AVAILABLE, "Available"),
        (NOT_AVAILABLE, "Not Available"),
        (ARCHIVED, "Archived"),
        (OUT_OF_STOCK, "Out of stock"),
    ]
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='static/img/')
    availability = models.CharField(max_length=13, choices=AVAILABILITY, default=AVAILABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.ForeignKey(ProductType, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('shop:product_info', args=[self.slug])

    def __str__(self):
        return self.name



