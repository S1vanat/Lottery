from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

url = "https://www.myhora.com/%E0%B8%AB%E0%B8%A7%E0%B8%A2/%e0%b8%aa%e0%b8%96%e0%b8%b4%e0%b8%95%e0%b8%b4%e0%b8%ab%e0%b8%a7%e0%b8%a2-%e0%b8%a2%e0%b9%89%e0%b8%ad%e0%b8%99%e0%b8%ab%e0%b8%a5%e0%b8%b1%e0%b8%87-30-%e0%b8%9b%e0%b8%b5.aspx?mode=year-range&value=30"
res = requests.get(url) #เอาทั้ง Web มาเก้็บในตัวแปร
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')#แปลงภาาาให้อ่านได้ทั้งหน้า
def get_text(list_text):
    """get if you want"""
    count = 0
    list_get_text = []
    for want in list_text:
        count += 1
        if count == 1 or count == 2 or count == 4:
            list_get_text.append(want)
        elif count == 6:
            list_get_text.append(want)
            count = 0
    return list_get_text

def add_in_dict(list_text):
    """add from list to dict and add key , id"""
    dict_reward = []
    data = {}
    num = 1
    for num_id in range(0, len(list_text), 4):
        data = {}
        data.update({'id' : num ,'day' : list_text[num_id - 4] + " " + list_text[num_id - 3] , 'year' : list_text[num_id - 2], 'one_reward': list_text[num_id - 1]})
        dict_reward.append(data)
        num += 1
    return dict_reward

def information():
    if res.status_code == 200:
        test = soup.find('div', attrs={'class' : 'lotto-left'})
        div_tag = test.findAll('div', attrs={'class': 'mt-10'})
        table = div_tag[1].find('table', attrs={'id' : 'dl_lottery_stats_list'})
        tr_tag = table.findAll('tr')
        list_text = []
        
        for team in tr_tag:
            rows = team.find('td')
            div_link = rows.find('div' , attrs={'class' : 'rowx div-link'})
            for txt in div_link:
                keep = []
                if txt.text.strip() != "":
                    list_text.append(txt.text.strip())
            for _ in range(6):
                list_text.pop()
        # -------------------------------------------------- get dict --------------------------------
        day_number = get_text(list_text)
        dict_daynumber = add_in_dict(day_number) 
        # ---------------- convert dict to json ------------
        json_str = json.dumps(dict_daynumber, ensure_ascii=False) # ensure_ascii=False แปลงภาษา ไม่ Encode
        json_file = open('data.reward.json', 'w')
        json_file.write(json_str)
        json_file.close()
    elif res.status_code == 404:
        print("Not found")
    else:
        print("Not both")
information()