from django.contrib import admin
from shop.models import Category, Product, ProductType


# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(ProductType)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "in_stock", "availability", "created", "updated"]
    list_filter = ["in_stock", "in_active"]
    list_editable = ["price", "in_stock"]
    prepopulated_fields = {"slug": ("name",)}
