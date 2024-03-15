from django.shortcuts import render

from goods.models import Products


def catalog(request):
    goods = Products.objects.all()
    context = {
        'title': 'Home - Catalog',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)


def product(request, slug=None, product_id=None):

    kwargs = {'slug': slug} if slug else {'id': product_id}
    product = Products.objects.get(**kwargs)
    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)
