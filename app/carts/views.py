from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products

# Create your views here.


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            cart.quntity += 1
            cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quntity=1)
    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product)

    return redirect(request.META.get('HTTP_REFERER'))


def cart_cnange(request, product_slug):
    ...


def cart_remove(request, product_slug):
    ...
