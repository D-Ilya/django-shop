from django.shortcuts import render
# from django.http import HttpResponse


def index(request):

    context: dict[str:any] = {
        'title': 'Home App',
        'content': 'Main page of shop',
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context: dict[str:any] = {
        'title': 'About Page',
        'content': 'About page content',
        'text_on_page': 'some label on page'
    }
    return render(request, 'main/about.html', context=context)
