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
    yeard = [y for y in range(2560, 2553, -1)]
    list_text = ['ลำดับ','วันที่','ปี','เลขรางวัลที่ 1','เลขหน้า 3 ตัว','เลขท้าย 3 ตัว','เลขท้าย 2 ตัว']
    context = {'j_file': j_file,
        'herder' : list_text,
        'count' : freq[1],
        'yeard' : yeard,
        'list_count' : zip(freq[1], freq[2]),
    }
    return render(request, 'allreward.html', context)

def frequency(j_file):
    """frequency of number"""
    keep_max_year = '2565'
    dict_count = {}
    list_all_num = []
    list_same_year = []
    year_dict = {}
    for num in j_file:
        list_all_num.append(num['one_reward'][4:])
        if keep_max_year == num['year']:
            list_same_year.append(num['one_reward'])
        else:
            list_same_year = []
            list_same_year.append(num['one_reward'])
            year_dict[num['year']] = list_same_year
            keep_max_year = num['year']
    reward_year = [year_dict]
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
    return list_header, sort_dict, list_count, reward_year


def percent(request):
    # หาความน่าจะเป็นที่จะเกิด ในนี่
    j_file = read_file_json()
    freq = frequency(j_file)
    reward_year = freq[3]
    zero = reward_year[0]
    count0, count1, count2, count3, count4, count5, count6, count7, count8, count9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    position = 0
    lak = 1
    year = 2560

    for _ in range(6):
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("0")
            if cal >= 1:
                count0 += 1
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("1")
            if cal >= 1:
                count1 += 1
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("2")
            if cal >= 1:
                count2 += 1
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("3")
            if cal >= 1:
                count3 += 1
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("4")
            if cal >= 1:
                count4 += 1
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("5")
            if cal >= 1:
                count5 += 1
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("6")
            if cal >= 1:
                count6 += 1
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("7")
            if cal >= 1:
                count7 += 1
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("8")
            if cal >= 1:
                count8 += 1
        for i in range(len(zero["2560"])):
            cal = zero["2560"][i][position]
            cal = cal.count("9")
            if cal >= 1:
                count9 += 1
        print("หลักที่ %d: %d %d %d %d %d %d %d %d %d %d" %(lak, count0, count1, count2, count3, count4, count5, count6, count7, count8, count9))
        position += 1
        lak += 1
        count0, count1, count2, count3, count4, count5, count6, count7, count8, count9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    context = {
        'data_reward' : reward_year,
    }
    
    return render(request, 'percent.html')

