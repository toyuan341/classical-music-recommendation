# -*- coding: utf-8 -*-
"""
web-scraping

Original file is located at
    https://colab.research.google.com/drive/174o-RyueXYBja0uwr7ndgyPmhzc_auvh
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib
from collections import Counter

# Define check function with variable-length arguments
def check(*variables):
    """ Check all elements from numbers"""
    print("="*30)
    for var in variables:
        print(f"Value: {var}")
        print(f"Type: {type(var)}")
        print("="*30)

# url A to Z
url_list = []
for i in range(ord('A'), ord('Z') + 1):
    a = f'https://www.naxos.com/musicinmovieslist.asp?letter={chr(i)}'
    url_list.append(a)

"""web scraping"""

def of_crawler(url0):
    """ get class """
    n0 = requests.get(url0)
    n1 = BeautifulSoup(n0.text, 'html.parser')
    return n1

def getM1(n4):
    """ get movie title """
    l = []
    for i in n4.find_all('td', attrs= {'bgcolor': '#EEEEEE'}):
        l.append(str(i.text))

    return l

def getPiece(n4):
    """ COMPOSER and piece """
    l = []
    for i in n4.find_all('td', attrs= {'class': 'style5'}):
        l.append(str(i.text))

    return l

"""1.** movie title**
\xa0 remove
list of lists(26)
"""

listM0 = []
for u in url_list:
    n0 = of_crawler(u)
    n1 = getM1(n0)
    listM0.append(n1)

list_movie = []
for i in listM0:
    list_movie.extend(i)

len(list_movie)

list_movie2 = []
for i in list_movie:
    list_movie2.append(i.replace('\xa0', ' '))

list_movie2

list_movie2[1200]

len(list_movie2)

"""composer and composition title"""

b_list = getPiece(of_crawler('https://www.naxos.com/musicinmovieslist.asp?letter=B'))
len(b_list)

b_list[1]

b_list2 = []
for i in b_list:
    s = i.strip('\n')
    b_list2.append(s.split('\n'))
b_list2

"""B: title*118, list item*119?"""

list_pie = []
for u in url_list:
    n0 = of_crawler(u)
    n1 = getPiece(n0)
    list_pie.append(n1)

check(list_pie)
# list_pie, len26

composition_list = []
for i in list_pie:
    for l in range(1, len(i)):
        composition_list.append(i[l])

len(composition_list)

composition_list[1559]

# list_comp will be a list of lists
list_comp = []
for i in composition_list:
    s = i.strip('\n')
    list_comp.append(s.split('\n'))
len(list_comp)

list_comp[20]

"""movie to compositions dictionary"""

# create a dictionary
title_dict = {}
for i in range(1560):
    k = list_movie2[i]
    v = list_comp[i]
    title_dict[k] = v
title_dict[list_movie2[20]]

"""all compositions"""

compTitle = []
for i in list_comp:
    compTitle.extend(i)
len(compTitle)

for i in range(300, 310):
    print(compTitle[i])

"""usage"""

c_counter = Counter(compTitle)
c_counter.most_common(10)

len(c_counter)

sum(c_counter.values())

check(c_counter)

# all composer-composition title
ct_list = []
for i in compTitle:
    if i in ct_list:
        pass
    else:
        ct_list.append(i)
len(ct_list)

"""計算曲目選用次數

"""

url_list2 = []
for i in range(ord('A'), ord('Z') + 1):
    a = f'https://www.naxos.com/musicinmoviescomplist.asp?letter={chr(i)}'
    url_list2.append(a)

def getName(n4):
    l = []
    for i in n4.find_all('td', attrs= {'bgcolor': '#EEEEEE'}):
        l.append(str(i.text))

    return l

def getTitle(n5):
    l = []
    for i in n5.find_all('div', attrs= {'style': 'border-top:1px dotted #999999; border-bottom:1px dotted #999999; padding:3px 0px; margin:0px 0px'}):
        l.append(str(i.text))

    return l

list_name = []
for u in url_list2:
    n0 = of_crawler(u)
    n1 = getName(n0)
    list_name.append(n1)
len(list_name)

for i in range(1, 2):
    print(list_name[i])

name_composer = []
for i in list_name:
    name_composer.extend(i)
len(name_composer)

cm_list = []
for u in url_list2:
    n0 = of_crawler(u)
    n1 = getTitle(n0)
    cm_list.append(n1)
len(cm_list)

for i in range(1, 3):
    print(cm_list[i])

len(cm_list[0])

list_cm = []
for i in cm_list:
    for l in i:
        s = l.strip('\n')
        list_cm.append(s[7:])
len(list_cm)

list_cm[1547]

titleMov = []
for i in list_cm:
    titleMov.append(i.split(' )'))
len(titleMov)

titleMov[1547]

cn_list = []
for i in list_cm:
    c = i.split(' )')
    cn_list.append(c[0] + ')')
cn_list[1547]

for i in range(len(titleMov)):
    for m in compTitle:
        if titleMov[i][0] in m:
            titleMov[i][0] = m
len(titleMov)

titleMov[1547]

titleMov[200]

mm_dict = {}
for i in titleMov:
    k = i[0]
    v = i[1].split(')  ')
    v2 = []
    for l in v:
        v2.append(l + ')')
    mm_dict[k] = v2
mm_dict[titleMov[200][0]]

mm_dict['BEETHOVEN Symphony No. 5 in C minor, Op. 67 (8.553476)']

#clean_list = []
#for i in range(len(titleMov)):
#    for m in list_movie2:
#        if m in titleMov[i][1]:
#           i.append



from google.colab import drive
drive.mount('/content/drive')

import requests
import pandas as pd
import io
import csv

mov_list = []
with open('/content/drive/MyDrive/IMdb.csv') as movF:
    movie_info = csv.reader(movF, delimiter='\t')
    for i in movie_info:
        mov_list.append(i)
mov_list[0]

mov_list2 = []
for i in mov_list:
    mov_list2.append(i[0].split(','))
mov_list2[1]

list_movie3 = []
for i in list_movie2:
    if ' (' in i:
        a = i.find(' (')
        list_movie3.append(i[:a])
    else:
        list_movie3.append(i)
list_movie3[18]

len(list_movie3)

list_movie3.index('O')

# all_mov2: [list_movie3, imdb movie title, year, genre]
all_mov2 = []
for i in mov_list2:
    for m in list_movie3:
        if m == i[3]:
            all_mov2.append([m, i[3], i[6], i[9]])
        elif (f'The {m}') == i[3]:
            all_mov2.append([m, i[3], i[6], i[9]])
len(all_mov2)

all_mov3 = []
for i in all_mov2:
    idx = list_movie3.index(i[0])
    if i[2] in list_movie2[idx]:
        i.insert(0, list_movie2[idx])
        all_mov3.append(i)
len(all_mov3)

for i in range(100, 108):
    print(all_mov3[i])

"""(1) all_mov3

(2) title_dict/ mm_dict

(3)
"""

# all_comp: [COMPOSER Title, Title]
all_comp = []
for i in ct_list:
    for n in cn_list:
        if n not in i:
            l = [i, 'None']
            pass
        else:
            l = [i, n]
            break
    all_comp.append(l)
len(all_comp)

all_comp[1]

# all_comp2: [COMPOSER Title, COMPOSER, Title]
all_comp2 = []
for i in all_comp:
    if i[1] != 'None':
        n = i[0].find(i[1])
        all_comp2.append([i[0], i[0][:n - 1], i[1]])
    else:
        all_comp2.append([i[0], 'None', 'None'])

all_comp2[32]

all_name = []
for i in all_comp2:
    all_name.append(i[1])
all_name2 = []
for n in all_name:
    if n not in all_name2:
        all_name2.append(n)
all_name2.remove('None')
all_name2[20]

for i in all_comp2:
    if i[1] == 'None':
        for n in all_name2:
            if n in i[0]:
                i[1] = n
len(all_comp2)

from google.colab import files

with open('movie.csv', 'w') as mov_file:
    writer = csv.writer(mov_file)
    writer.writerows(all_mov3)
files.download('movie.csv')

with open('composition.csv', 'w') as com_file:
    writer = csv.writer(com_file)
    writer.writerows(all_comp2)
files.download('composition.csv')

with open('movie_to_music.csv', 'w') as mm_file:
    writer = csv.writer(mm_file)
    for key, value in title_dict.items():
        writer.writerow([key, value])
files.download('movie_to_music.csv')

with open('music_to_movie.csv', 'w') as MM_file:
    writer = csv.writer(MM_file)
    for key, value in mm_dict.items():
        writer.writerow([key, value])
files.download('music_to_movie.csv')