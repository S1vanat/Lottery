from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
import random as r
from django.template import Context, Template
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
    # number_count = 1
    # if 'count' in request.session:
    #     number_count = request.session['count']
    # else:
    #     request.session['count'] = 1
    random_number = r.randrange(100000, 1000000)
    list_text = ['ลำดับ','เลขรางวัลที่ 1','เลขหน้า 3 ตัว','เลขท้าย 3 ตัว','เลขท้าย 2 ตัว']
    context = {
        'random_number' : random_number,
        'two_num_last' : str(random_number)[4:],
        'three_num_first' : str(random_number)[:3],
        'three_num_last' : str(random_number)[3:],
        'herder' : list_text,
        }
    return render(request, 'randompage.html' ,context)

def allreward(request):
    return render(request, 'allreward.html',)