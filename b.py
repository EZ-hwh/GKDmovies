from bs4 import BeautifulSoup
import urllib.request

res = urllib.request.urlopen('https://movie.douban.com/celebrity/1274477/')
html = res.read().decode('utf-8')
#print(f.read())
soup = BeautifulSoup(html,'html.parser') 
#name = soup.find('h1').span.text
#print(name)
'''
pic = soup.find('a',class_='nbg')
with open('1.jpg','wb') as f:
        #print(pic.find('img')['src'])
        import requests
        r = requests.get(pic.find('img')['src'])
        f.write(r.content)
'''
info = soup.find(class_='info')
for d in info.findAll('li'):
        #del d.find('li')
        #del d['span']
        print(d.get_text())
#intro = soup.find(class_='related-info')
#print(intro.span.text)