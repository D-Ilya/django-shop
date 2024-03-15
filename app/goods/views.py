from django.shortcuts import get_object_or_404, render

from goods.models import Products


def catalog(request, category_slug):
    goods = Products.objects.all() \
        if category_slug == 'all' \
        else get_object_or_404(Products.objects.filter(category_id__slug=category_slug))
    context = {
        'title': 'Home - Catalog',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slag=None, product_id=None):
    kwargs = {'slug': product_slag} \
        if product_slag  \
        else {'id': product_id}
    product = Products.objects.get(**kwargs)
    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)
