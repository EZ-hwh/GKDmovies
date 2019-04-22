#env/usr/bin python
#encoding:utf-8
'''
功能：抽取html中的链接
'''
'''
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
'''
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
df = pd.read_csv('top250_movie.csv',sep='#',encoding='utf8')

for i in range(250):
    res = urllib.request.urlopen(df['movie_url'][i])
    #res = urllib.request.urlopen(a['href'][0:46])
    html = res.read().decode('utf-8')
    s=BeautifulSoup(html)
    name1=s.findAll('h1')
    for n in name1:

        print(n.span.text)
        soup = BeautifulSoup(html,'html.parser') 
        name = soup.find('h1').span.text
        print(name)
        '''
        pic = soup.find('a',class_='nbgnbg')
        with open(n.span.text+'.jpg','wb') as f:
            import requests
            r = requests.get(pic.find('img')['src'])
            f.write(r.content)
        '''

        info = soup.find(id='info')
        for d in info.findAll('span'):
            if (d.find(class_='pl')):
                if(d.find(class_='pl').string=='导演'):
                    for e in d.findAll('a'):
                        print(e['href']+' '+e.string)
                elif(d.find(class_='pl').string=='演员'):
                    for e in d.findAll('a'):
                        print(e['href']+' '+e.string)

        detail = info.get_text()
        for i in detail.split('\n'):
            #print(i)
            j=i.split(':')
            if (j[0]=='类型'):
                    print(j[1])
            elif (j[0]=='制片国家/地区'):
                    print(j[1])
            elif (j[0]=='语言'):
                    print(j[1])
            elif (j[0]=='上映日期'):
                    print(j[1])
            elif (j[0]=='片长'):
                    print(j[1])
            elif (j[0]=='又名'):
                    print(j[1])
            elif (j[0]=='IMDb链接'):
                    print(j[1])

        intro = soup.find(class_='related-info')
        print(intro.span.text.replace("\n","").replace("\r",""))
        

f.close()

