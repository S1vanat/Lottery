from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
import random as r
from django.template import Context, Template
import json

# Create your views here.
def home(request):
    """rander to page home"""
    context = {'namae' : "Thanawath Petavibornsatarn",
        'age' : '15',
        'bd' : '20/04/2012'
    }
    return render(request, 'index.html', context)

def page1(request):
    """rander to page1"""
    return render(request, 'page1.html')

def randompage(request):
    """random number in random"""
    random_number = r.randrange(000000, 1000000)
    list_text = ['เลขรางวัลที่ 1','เลขหน้า 3 ตัว','เลขท้าย 3 ตัว','เลขท้าย 2 ตัว']
    context = {
        'random_number' : random_number,
        'herder' : list_text,
        }
    return render(request, 'randompage.html' ,context)

def read_file_json():
    """read file json"""
    a = open('data_reward.json', encoding="utf8")
    data = json.load(a)
    return data

def allreward(request):
    """show header and show data number"""
    j_file = read_file_json()
    freq = frequency(j_file)
    yeard = [y for y in range(2564, 2553, -1)]
    list_text = ['ลำดับ','วันที่','ปี','เลขรางวัลที่ 1','เลขหน้า 3 ตัว','เลขท้าย 3 ตัว','เลขท้าย 2 ตัว']
    context = {'j_file': j_file,
        'herder' : list_text,
        'count' : freq[1],
        'yeard' : yeard,
        'list_count' : zip(freq[0], freq[2]),
    }
    return render(request, 'allreward.html', context)

def frequency(j_file):
    """frequency of number"""
    dict_count = {}
    list_all_num = []

    for num in j_file:
        list_all_num.append(num['one_reward'][4:])

    # get dict number reward 

    for key in list_all_num:
        count = 0
        if (key in dict_count):
            count = dict_count[key]
        dict_count[key] = count + 1
    sort_dict = dict(sorted(dict_count.items(), key=lambda x: x[1]))
    # sorted by values
    sort_by_values = sorted(dict_count.items(), key=lambda x: x[1])
    list_count = []
    concat_num = ""
    keep = 1
    for s_time in sort_by_values:
        if s_time[1] == keep:
            concat_num = concat_num + s_time[0] + " "
        else:
            list_count.append(concat_num)
            keep = s_time[1]
            concat_num = ""
    list_header = [str(index) + " " + "ครัง" for index in range(1,len(list_count)+1)]
    return list_header, sort_dict, list_count


def percent(request, j_file):
    return render(request, 'percent.html')

