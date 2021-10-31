from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
import random as r
# Create your views here.
def home(request):
    context = {'namae' : "Thanawath Petavibornsatarn",
        'age' : '15',
        'bd' : '20/04/2012'
    }
    return render(request, 'index.html', context)

def page1(request):
    return render(request, 'page1.html')

def randompage(request):
    random_number = r.randrange(100000, 1000000)
    
    return render(request, 'randompage.html', {'random_number' : random_number})