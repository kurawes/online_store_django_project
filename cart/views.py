from django.shortcuts import render
from .models import Cart


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("New Cart created")
    return cart_obj


def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    queryset = Cart.objects.filter(id=cart_id)
    if queryset.count() == 1:
        print("Card Id exists")
        cart_obj = queryset.first()
    else:
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id
    return render(request, "cart_home.html", {})
