#env/usr/bin python
#encoding:utf-8

rubbish=["曾心怡","吴念真","张育邦","孙靖","韩冬","Mark Phoenix","Emma Field-Rayner","Paolo Carlini","Margaret Rawlings","Rod Myers","Scott Joel Gizicki","詹姆斯·凯伦","布莱恩·豪威","杜汶泽","Niall O'Brien","Luigi De Luca"]
#print(rubbish[0])

import random
from GKDmovies.wsgi import *
from search.models import *

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
df = pd.read_csv('top250_movie.csv',sep='#',encoding='utf8')
def movie():
        Movie.objects.all().delete()
        for i in range(250):
                res = urllib.request.urlopen(df['movie_url'][i])
                #res = urllib.request.urlopen(a['href'][0:46])
                html = res.read().decode('utf-8')
                s=BeautifulSoup(html)
                name1=s.findAll('h1')
                for n in name1:

                        #print(n.span.text)
                        soup = BeautifulSoup(html,'html.parser') 
                        name = soup.find('h1').span.text
                        print(name)
                        number = str(random.randint(1000000,9999999))
                        pic = soup.find('a',class_='nbgnbg')

                        with open(number+'.jpg','wb') as f:
                                import requests
                                r = requests.get(pic.find('img')['src'])
                                f.write(r.content)
                        
                        photo = "movieset/"+number+'.jpg'
                        
                        info = soup.find(id='info')
                        '''
                        for d in info.findAll('span'):
                                if (d.find(class_='pl')):
                                        if(d.find(class_='pl').string=='导演'):
                                                for e in d.findAll('a'):
                                                        Direct.objects.get_or_create(movie_name = name,director_name = e.string)
                                                        #print(e.string)
                                                        #print(e['href']+' '+e.string)
                                        elif(d.find(class_='pl').string=='主演'):
                                                for e in d.findAll('a'): 
                                                        Play.objects.get_or_create(movie_name = name,actor_name = e.string) 
                                                        #print(e.string)
                                                        #print(e['href']+' '+e.string)
                        '''
                        detail = info.get_text()
                        type=''
                        language=''
                        intro=''
                        place=''
                        length=''
                        rename=''
                        for i in detail.split('\n'):
                                #print(i)
                                j=i.split(':')
                                if (j[0]=='类型'):
                                        type=j[1]
                                elif (j[0]=='制片国家/地区'):
                                        place=j[1]
                                elif (j[0]=='语言'):
                                        language=j[1]
                                elif (j[0]=='上映日期'):
                                        movie_date=j[1]
                                elif (j[0]=='片长'):
                                        length=j[1]
                                elif (j[0]=='又名'):
                                        rename=j[1]
                                #elif (j[0]=='IMDb链接'):
                                #        print(j[1])

                        intro1 = soup.find(class_='related-info')
                        intro = intro1.span.text.replace("\n","").replace("\r","")
                        Movie.objects.get_or_create(movie_name=name,movie_date=movie_date,intro=intro,type=type,place=place,language=language,length=length,rename=rename,photo=photo)

def a(html):
        soup = BeautifulSoup(html,'html.parser') 
        if (not soup.find('h1')):
                return False
        name = soup.find('h1').text.split(' ')[0]
        print(name)
        number = str(random.randint(1000000,9999999))
        pic = soup.find('a',class_='nbg')
        with open(number+'.jpg','wb') as f:
                #print(pic.find('img')['src'])
                import requests
                r = requests.get(pic.find('img')['src'])
                f.write(r.content)
        gender = ''
        birthdate = ''
        constellation = ''
        birthplace = ''
        occupation = ''
        photo = "personset/"+number+'.jpg'

        info = soup.find(class_='info')
        for d in info.findAll('li'):
                j = d.get_text().strip().split(':')
                #print(j[0],j[1].strip())
                if (j[0]=='性别'):
                        if (j[1].strip()=='男'):
                                gender='m'
                        else:
                                gender='f'
                elif (j[0]=='星座'):
                        constellation = j[1].strip()
                elif (j[0]=='出生日期'):
                        birthdate = j[1].strip()
                elif (j[0]=='出生地'):
                        birthplace = j[1].strip()
                elif (j[0]=='职业'):
                        occupation = j[1].strip()
                #print(d.get_text())
        c=''
        intro = soup.find(id='intro')
        if (intro.find(class_='all-hidden')):
                c=intro.find(class_='all hidden').text
        else:
                c=intro.find(class_='bd').text
        intro = soup.find(class_='all hidden')
        Person.objects.get_or_create(name=name,intro=c.strip(),constellation=constellation,gender=gender,birthdate=birthdate,birthplace=birthplace,occupation=occupation,photo=photo)
        return True

def person():
        #Person.objects.all().delete()
        #Play.objects.all().delete()
        #Direct.objects.all().delete()

        for i in range(3,5):
                res = urllib.request.urlopen(df['movie_url'][i])
                html = res.read().decode('utf-8')
                #print(html)
                s=BeautifulSoup(html)
                name1=s.findAll('h1')
                for n in name1:

                        #print(n.span.text)
                        soup = BeautifulSoup(html,'html.parser') 
                        name = soup.find('h1').span.text
                        print(name)
                        info = soup.find(id='info')
                        for d in info.findAll('span'):
                                if (d.find(class_='pl')):
                                        if(d.find(class_='pl').string=='导演'):
                                                for e in d.findAll('a'):
                                                        print(e.string.strip())
                                                        if (not Person.objects.filter(name=e.string.strip())):                                                           
                                                                res = urllib.request.urlopen('https://movie.douban.com'+e['href'])
                                                                #print('https://movie.douban.com'+e['href'])
                                                                html = res.read().decode('utf-8')    
                                                                a(html)
                                                        Direct.objects.get_or_create(movie_name = Movie.objects.get(movie_name=name),director_name = Person.objects.get(name=e.string.strip()))
                                                        
                                        elif(d.find(class_='pl').string=='主演'):
                                                t = True
                                                for e in d.findAll('a'): 
                                                        print(e.string.strip())
                                                        if (e.string not in rubbish)and(' ' not in e.string):
                                                                if (not Person.objects.filter(name=e.string.strip())):                                                           
                                                                        res = urllib.request.urlopen('https://movie.douban.com'+e['href'])
                                                                        html = res.read().decode('utf-8')    
                                                                        t = a(html)
                                                                if t:
                                                                        Play.objects.get_or_create(movie_name = Movie.objects.get(movie_name=name),actor_name = Person.objects.get(name=e.string.strip()))                                                         

person()
