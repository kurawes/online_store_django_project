from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    objects = models.Manager()

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=30)
    objects = models.Manager()

    def __str__(self):
        return self.name


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
    description = models.TextField()
    picture = models.ImageField(upload_to='static/img/')
    availability = models.CharField(max_length=13, choices=AVAILABILITY, default=AVAILABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    objects = models.Manager()

    def __str__(self):
        return self.name



