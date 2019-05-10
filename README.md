# README

### 灵感来源
该项目的灵感来自于豆瓣电影，目标是实现一个电影影评网站，主要提供对电影、演员、导演的搜索功能，能查看每部电影、每位演员和导演的具体信息，并可以对电影进行打分和评论，为爱好电影的人们提供一个公共的交流和分享看法的平台。

### 环境
```
	Python 3.7.0
	Django 2.2.0
```

### 使用方法
```
# Clone this repository
$ git clone https://github.com/EZ-hwh/GKDmovies.git

# Go into the repository
$ cd GKDmovies

# Add new movie from Douban (an example)
$ python add.py 
$ https://movie.douban.com/subject/26835471/

# Run server
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
April 28, 2019 - 23:27:10
Django version 2.2.0, using settings 'GKDmovies.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 主要功能
1. 搜索电影、演员或导演。
2. 查看电影、演员或导演的具体信息
3. 用户的注册、登录、登出
4. 用户登录后可以对电影进行打分和评论
5. 修改用户的个人资料

### 参考文献
Django官方文档 
	https://docs.djangoproject.com/zh-hans/2.1/contents/
环形图的模板来源
	https://www.highcharts.com.cn/demo/highcharts/pie-donut-center-title

---
GKDmovies for Database 2019 Spring @ Fudan University, by [**Chenhao Wang**](<https://github.com/wch19990119>) Wang and [**Wenhao Huang**](<https://github.com/EZ-hwh>)