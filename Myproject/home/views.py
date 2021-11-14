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
    freq = frequency(j_file)
    list_text = ['ลำดับ','วันที่','ปี','เลขรางวัลที่ 1','เลขหน้า 3 ตัว','เลขท้าย 3 ตัว','เลขท้าย 2 ตัว']
    context = {'j_file': j_file,
    'herder' : list_text,
    }
    return render(request, 'allreward.html', context)

def frequency(j_file):
    dict_count = {}
    list_all_num = []
    for num in j_file:
        list_all_num.append(num['one_reward'][4:])

    for key in list_all_num:
        count = 0
        if (key in dict_count):
            count = dict_count[key]
        dict_count[key] = count + 1
    sort_dict = dict(sorted(dict_count.items()))
    
# 795283  5
# 800000  6
# {795283:count}
# 1 : เลข เลข เลข เลข
# 2 : เลข เลข เลข เลข