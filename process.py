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
                        number = str(random.randint(100000,999999))
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
        intro = soup.find(class_='all hidden')
        Person.objects.get_or_create(name=name,intro=intro.text,constellation=constellation,gender=gender,birthdate=birthdate,birthplace=birthplace,occupation=occupation,photo=photo)

def person():
        #Person.objects.all().delete()

        for i in range(250):
                res = urllib.request.urlopen(df['movie_url'][i])
                html = res.read().decode('utf-8')
                print(html)
                s=BeautifulSoup(html)
                name1=s.findAll('h1')
                for n in name1:

                        print(n.span.text)
                        soup = BeautifulSoup(html,'html.parser') 
                        name = soup.find('h1').span.text
                        print(name)
                        info = soup.find(id='info')
                        
                        for d in info.findAll('span'):
                                if (d.find(class_='pl')):
                                        if(d.find(class_='pl').string=='导演'):
                                                for e in d.findAll('a'):
                                                        if (not Person.objects.filter(name=e.string)):                                                           
                                                                res = urllib.request.urlopen(e['href'])
                                                                html = res.read().decode('utf-8')    
                                                                a(e.string)
                                                        Direct.objects.get_or_create(movie_name = Movie.objects.filter(movie_name=name),director_name = Person.objects.filter(name=e.string))
                                                        
                                        elif(d.find(class_='pl').string=='主演'):
                                                for e in d.findAll('a'): 
                                                        if (not Person.objects.filter(name=e.string)):                                                           
                                                                res = urllib.request.urlopen(e['href'])
                                                                html = res.read().decode('utf-8')    
                                                                a(e.string)
                                                        Play.objects.get_or_create(movie_name = Movie.objects.filter(movie_name=name),actor_name = Person.objects.filter(name=e.string))                                                         

person()