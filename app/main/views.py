from django.shortcuts import render
# from django.http import HttpResponse

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()
    context: dict[str:any] = {
        'title': 'Home App',
        'content': 'Main page of shop',
        'categories': categories
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context: dict[str:any] = {
        'title': 'About Page',
        'content': 'About page content',
        'text_on_page': 'some label on page'
    }
    return render(request, 'main/about.html', context=context)
