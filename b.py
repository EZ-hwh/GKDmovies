from bs4 import BeautifulSoup
import urllib.request
chaper_url='https://movie.douban.com/celebrity/1274477/'
#headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/201'}

#req = urllib.request.Request(url=chaper_url, headers=headers)
#html = urllib.request.urlopen(req).read().decode('utf-8')
#res = urllib.request.urlopen(url=',headers=headers)
#html = res.read().decode('utf-8')
f = open('b.txt','r')
html= f.read()

soup = BeautifulSoup(html,'html.parser') 
name = soup.find('h1').text.split(' ')[0]
print(name)
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
        j = d.get_text().strip().split(':')
        #print(j[0],j[1].strip())
        if (j[0]=='性别'):
                if (j[1].strip()=='男'):
                        print('m')
                else:
                        print('f')
        elif (j[0]=='星座'):
                print(j[1].strip())
        elif (j[0]=='出生日期'):
                print(j[1].strip())
        elif (j[0]=='出生地'):
                print(j[1].strip())
        elif (j[0]=='职业'):
                print(j[1].strip())
        #print(d.get_text())
intro = soup.find(id='intro')
if (intro.find(class_='all-hidden')):
        print(intro.find(class_='all hidden').text)
else:
        print(intro.find(class_='bd').text)