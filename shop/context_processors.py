from .models import ProductType, Category


# context processor - to see all the categories everywhere, add to settings.py TEMPLATES
def categories(request):
    return {"categories": Category.objects.all()}


# context processor - to see all the product types everywhere, add to settings.py TEMPLATES
def product_types(request):
    return {"product_types": ProductType.objects.all()}