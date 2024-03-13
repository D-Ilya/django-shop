# from urllib import response
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    context: dict[str:any] = {
        'title': 'Home',
        'content': 'Main page of shop',
        'list': ['first', 'second', 'third'],
        'dict': {1: 'one', 2: 'two', 3: 'three'},
        'bool': True
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'about/index.html')
