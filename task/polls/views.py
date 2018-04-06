from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


def index(request):
    return render(request,'polls/index.html')

def login(request):
    if request.method == 'POST':
        return
    else:
        return render(request, 'polls/login.html')

def register(request):
    if request.method == 'POST':
        return
    else:
        return render(request,'polls/register.html')
