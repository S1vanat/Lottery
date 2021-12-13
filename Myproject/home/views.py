from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
import random as r
from django.template import Context, Template
import json
import math
import csv

# Create your views here.
def home(request):
    """rander to page home"""
    context = {'namae' : "Thanawath Petavibornsatarn",
        'age' : '15',
        'bd' : '20/04/2012'
    }
    return render(request, 'index.html', context)

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
    yeard = [y for y in range(2554, 2553, -1)]
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
    list_sequence = ["เลข 0", "เลข 1", "เลข 2", "เลข 3", "เลข 4", "เลข 5", "เลข 6", "เลข 7", "เลข 8", "เลข 9"]
    list1 = []
    list2 = []
    list3 = []
    list_year = []
    for j in range(2554,2565):
        list_year.append(j)
        year = str(j) + ""
        for _ in range(6):
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("0")
                if cal >= 1:
                    count0 += 1
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("1")
                if cal >= 1:
                    count1 += 1
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("2")
                if cal >= 1:
                    count2 += 1
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("3")
                if cal >= 1:
                    count3 += 1
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("4")
                if cal >= 1:
                    count4 += 1
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("5")
                if cal >= 1:
                    count5 += 1
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("6")
                if cal >= 1:
                    count6 += 1
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("7")
                if cal >= 1:
                    count7 += 1
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("8")
                if cal >= 1:
                    count8 += 1
            for i in range(len(zero[year])):
                cal = zero[year][i][position]
                cal = cal.count("9")
                if cal >= 1:
                    count9 += 1
            count0 = math.ceil((count0/len(zero[year]))*100)
            count1 = math.ceil((count1/len(zero[year]))*100)
            count2 = math.ceil((count2/len(zero[year]))*100)
            count3 = math.ceil((count3/len(zero[year]))*100)
            count4 = math.ceil((count4/len(zero[year]))*100)
            count5 = math.ceil((count5/len(zero[year]))*100)
            count6 = math.ceil((count6/len(zero[year]))*100)
            count7 = math.ceil((count7/len(zero[year]))*100)
            count8 = math.ceil((count8/len(zero[year]))*100)
            count9 = math.ceil((count9/len(zero[year]))*100)
            list1.append(count0)
            list1.append(count1)
            list1.append(count2)
            list1.append(count3)
            list1.append(count4)
            list1.append(count5)
            list1.append(count6)
            list1.append(count7)
            list1.append(count8)
            list1.append(count9)

            # print("หลักที่ %d: %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f" %(lak, count0, count1, count2, count3, count4, count5, count6, count7, count8, count9))
            # เก็บตัวแปลลิส
            position += 1
            lak += 1
            list2.append(list1)
            count0, count1, count2, count3, count4, count5, count6, count7, count8, count9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            list1 = []
        list3.append(list2)
        list2 = []
        position = 0
        lak = 1
    context = {
        'data_reward' : reward_year,
        'list3' : zip(list3, list_year),
        'list_sequence' : list_sequence,
    }

    return render(request, 'percent.html', context)
def percent_per_year():
    """find perccent per year for grah"""
    list_coust = [[18,12,16,13,19,20,9,9,15,13],[5,8,9,6]]
    keep_list = []
    for num_count in list_coust:
        list_empty = []
        for num_per in num_count:
            list_empty.append((num_per / 144) * 100)
        keep_list.append(list_empty)
    return keep_list

def page1(request):
    """rander to page1"""
    with open('names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])
    return render(request, 'page1.html')

