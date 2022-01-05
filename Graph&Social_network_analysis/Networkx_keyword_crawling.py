# 연관어 분석을 위한 크롤링을 실시한다.
import bs4
import pandas as pd
import numpy as np
import re
import requests
from bs4 import BeautifulSoup

word = '코로나'
url_based = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q='
url = url_based + word
r = requests.get(url)
print(r)
soup = bs4.BeautifulSoup(r.text, 'lxml')
first_keywords = soup.find_all("a",{"class":"keyword"})
df = pd.DataFrame(columns = ['first', 'second', 'third'])
keywords = []
for f in first_keywords:
    first = f.text
    url_second = url_based + first
    r2 = requests.get(url_second)
    soup_second = bs4.BeautifulSoup(r2.text, 'lxml')
    second_keywords = soup_second.find_all("a",{"class":"keyword"})

    for s in second_keywords:
        second = s.text
        url_third = url_based + second
        r3 = requests.get(url_third)
        soup_third = bs4.BeautifulSoup(r3.text, 'lxml')
        third_keywords = soup_second.find_all("a", {"class": "keyword"})

        for t in third_keywords:
            third = t.text
            keywords.append([first, second, third])

for i in range(len(keywords)):
    df.loc[i] = keywords[i]

df.to_csv('keyword_corona.csv')