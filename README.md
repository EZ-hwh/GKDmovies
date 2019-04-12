# GKDmovies
### 数据库的关系模式
##### 属性值：
电影：电影名，演员姓名，导演姓名，上映日期，评论，评分，类型，剧情简介，照片，浏览
演员：姓名，电影名，基本介绍，性别
导演：姓名，电影名，基本介绍，性别
用户：评论，电影名，评分，好友，账户名，密码，浏览，个性签名

##### 关系模式：
movie(movie_name,date,director_name,synopsis，photo)
actor(actor_name,gender,actor_intro)
director(director_name,gender,director_intro)
user(user_name,password,signature)

play(movie_name,actor_name)
label(movie_name,label)
comment(movie_name,user_name,comment,grade)
friend(user_name,user_name)
skim(movie_name,user_name,date)