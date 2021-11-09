from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
import random as r
from django.template import Context, Template
import json

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
    random_number = r.randrange(000000, 1000000)
    list_text = ['ลำดับ','เลขรางวัลที่ 1','เลขหน้า 3 ตัว','เลขท้าย 3 ตัว','เลขท้าย 2 ตัว']
    context = {
        'random_number' : random_number,
        'herder' : list_text,
        }
    return render(request, 'randompage.html' ,context)

def reaad_file_json():
    a = open('data_reward.json', encoding="utf8")
    data = json.load(a)
    return data

def allreward(request):
    j_file = reaad_file_json()
    list_text = ['ลำดับ','วันที่','ปี','เลขรางวัลที่ 1','เลขหน้า 3 ตัว','เลขท้าย 3 ตัว','เลขท้าย 2 ตัว']
    context = {'j_file': j_file,
    'herder' : list_text,
    }
    # print(j_file)
    return render(request, 'allreward.html', context)

# [{ id: 1, day : 1 day , year : }]