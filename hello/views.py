from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    params = {
        'title': 'Hello/Index',
        'msg': ' お名前は？',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)


def form(request):
    msg = request.POST['msg']
    params = {
        'title': 'Hello/Form',
        'msg': 'こんにちは、' + msg + 'さん',
    }
    return render(request, 'hello/index.html', params)


def next(request):
    params = {
        'title': 'Hello/Next',
        'msg': ' これは、もう1つのページです。',
        'goto': 'index',
    }
    return render(request, 'hello/index.html', params)
