from django.shortcuts import render


# def goods(request):
#     context: dict[str:any] = {
#         'title': 'Goods Page',
#         'content': 'Goods page content',
#         'text_on_page': 'some goods on page'
#     }
#     return render(request, 'main/about.html', context=context)


def catalog(request):
    return render(request, 'goods/catalog.html')


def product(request):
    return render(request, 'goods/product.html')
