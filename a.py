#coding:utf-8
from bs4 import BeautifulSoup
import urllib.request

res = urllib.request.urlopen('https://movie.douban.com/subject/1296753/')
html = res.read().decode('utf-8')
#print(f.read())
soup = BeautifulSoup(html,'html.parser') 
name = soup.find('h1').span.text
print(name)
'''
pic = soup.find('a',class_='nbgnbg')
with open('1.jpg','wb') as f:
        #print(pic.find('img')['src'])
        import requests
        r = requests.get(pic.find('img')['src'])
        f.write(r.content)
'''
info = soup.find(id='info')

for d in info.findAll('span'):
    if (d.find(class_='pl')):
        print(d.find(class_='pl').string)
        for e in d.findAll('a'):
            print(e['href']+' '+e.string)

detail = info.get_text()
for i in detail.split('\n'):
        print(i)
        j=i.split(':')
        if (j[0]=='类型'):
                print('1')
        elif (j[0]=='制片国家/地区'):
                print('2')
        elif (j[0]=='语言'):
                print('3')
        elif (j[0]=='上映日期'):
                print('4')
        elif (j[0]=='片长'):
                print('5')
        elif (j[0]=='又名'):
                print('6')
        elif (j[0]=='IMDb链接'):
                print('7')
intro = soup.find(class_='related-info')
print(intro.span.text)