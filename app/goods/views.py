from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.utils import q_search
from goods.models import Products


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)

    goods = None
    if query := request.GET.get('q'):
        goods = q_search(query)
    else:
        goods = (
            Products.objects.all()
            if category_slug == 'all'
            else get_list_or_404(Products.objects.filter(
                category_id__slug=category_slug)
            )
        )

    if request.GET.get('on_sale', None):
        goods = goods.filter(discount__gt=0)

    if (order_by := request.GET.get('order_by')) and order_by != 'default':
        goods = goods.order_by(order_by)

    p = Paginator(goods, 3)
    current_page = p.page(page)
    context = {
        'title': 'Home - Catalog',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug=None, product_id=None):
    kwargs = {'slug': product_slug} \
        if product_slug  \
        else {'id': product_id}
    product = Products.objects.get(**kwargs)
    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)
