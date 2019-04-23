from django.http import HttpResponse,Http404
from .models import *
from django.shortcuts import render,get_object_or_404
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.

def Frontpage(request):
    return render(request, "Frontpage.html",{'photo':'timg.jpeg'})

def search(request):
    q = request.GET.get('index')
    p = request.GET.get('person')

    error_msg = ''

    if not q:
        #error_msg = '请输入关键词'
        return render(request, 'Frontpage.html', {'error_msg': error_msg})
		
    if p == 'all' or not p:
        actor_list = Actor.objects.filter(actor_name__contains=q).order_by('actor_name')
        movie_list = Movie.objects.filter(movie_name__contains=q).order_by('movie_name')
        director_list = Director.objects.filter(director_name__contains=q).order_by('director_name')
        return render(request, 'results.html', {'error_msg': error_msg, 'actor_list': actor_list , 'movie_list': movie_list , 'director_list': director_list})

    if p == 'actor' :
        actor_list = Actor.objects.filter(actor_name__contains=q).order_by('actor_name')
        return render(request, 'results.html', {'error_msg': error_msg, 'actor_list': actor_list})
    
    if p == 'movie' :
        movie_list = Movie.objects.filter(movie_name__contains=q).order_by('movie_name')
        return render(request, 'results.html', {'error_msg': error_msg, 'movie_list': movie_list})

    if p == 'director' :
        director_list = Director.objects.filter(director_name__contains=q).order_by('director_name')
        return render(request, 'results.html', {'error_msg': error_msg, 'director_list': director_list})
	
def actor(request):
    q = request.GET.get('actor_name')
    actor = Actor.objects.get(actor_name=q)
    movie = Play.objects.filter(actor_name=q)
    return render(request, 'actor.html', {'actor': actor, 'movie': movie})

def movie(request): 
    q = request.GET.get('movie_name')
    login = request.session.get('login',None)
    user = request.session.get('user_name',None)
    movie = Movie.objects.get(movie_name=q)
    director = Direct.objects.filter(movie_name=q)
    actor = Play.objects.filter(movie_name=q)
    comment = Comment.objects.filter(movie_name=q)
    
    if not login:
        return render(request, 'movie.html', {'actor': actor, 'director': director, 'movie': movie, 'comment': comment})
        
    if Comment.objects.filter(user_name=user) : 
        return render(request, 'movie.html', {'actor': actor, 'director': director, 'movie': movie, 'comment': comment})
    
    n_exist = True   
    return render(request, 'movie.html', {'actor': actor, 'director': director, 'movie': movie, 'comment': comment, 'n_exist': n_exist})  
    
    

def director(request):
    q = request.GET.get('director_name')
    director = Director.objects.get(director_name=q)
    movie = Movie.objects.filter(director_name=q)
    return render(request, 'director.html', {'director': director, 'movie': movie})

def user(request):
    q = request.session['user_name']
    user = User.objects.get(user_name=q)
    return render(request, 'user.html', {'user': user})    
 
def actor_all(request):
    actor_list = Actor.objects.all()
    return render(request, 'results.html', {'actor_list': actor_list})
	
def movie_all(request):
    movie_list = Movie.objects.all()
    return render(request, 'results.html', {'movie_list': movie_list})
    
def director_all(request):
    director_list = Director.objects.all()
    return render(request, 'results.html', {'director_list': director_list})

def login(request):
    return render(request, 'login.html', {})

def logout(request):
    request.session.flush()
    return render(request, 'Frontpage.html', {}) 
    
def register(request):
    return render(request, 'register.html', {})
    
def add_user(request):
    user = request.GET.get('user')
    password = request.GET.get('password')
    password2 = request.GET.get('password2')
    if not user :
        message = '用户名不能为空！'
        return render(request, 'register.html', {'message': message})
    if not password or not password2 :
        message = '密码不能为空！'
        return render(request, 'register.html', {'message': message})
    if password != password2 :
        message = '两次密码输入不相符！'
        return render(request, 'register.html', {'message': message})
    
    try :
        q = User.objects.get(user_name=user)   
    except User.DoesNotExist :
        if password == password2 :
            q = User()
            q.user_name = user
            q.password = password
            q.save()
            message = '注册成功！'
            success = 'success'
            return render(request, 'register.html', {'message': message, 'success':success})
        
    message = '该用户名已被使用！'
    return render(request, 'register.html', {'message': message})
    
def check(request):
    user = request.GET.get('user')
    password = request.GET.get('password')
    if not user :
        message = '用户名不能为空！'
        return render(request, 'login.html', {'message': message})
    if not password :
        message = '密码不能为空！'
        return render(request, 'login.html', {'message': message})
        
    try :
        q = User.objects.get(user_name=user)   
    except User.DoesNotExist :
        message = '用户不存在！'
        return render(request, 'login.html', {'message': message})
        
    if q.password != password :
        message = '密码错误！'
        return render(request, 'login.html', {'message': message})
    if q.password == password :
        message = '登录成功！'
        success = 'success'
        request.session['login'] = True
        request.session['user_name'] = user
        request.session['password'] = password           
        return render(request, 'login.html', {'message': message,'success':success})

def add_comment(request): #wrong
    
    q = request.GET.get('movie_name')
    p = request.session.get('user_name',None)
    grade = request.GET.get('score')
    comment = request.GET.get('comment')
      
    #if not comment :
    
    movie = Movie.objects.get(movie_name=q)   
    user = User.objects.get(user_name=p)
    Comment.objects.create(movie_name=movie,user_name=user,grade=grade,comment=comment)
    
    return redirect('/movie/?movie_name=%s' % (movie.movie_name)) 
    

    
def delete_comment(request): #wrong  
    movie = request.GET.get('movie_name')
    user = request.GET.get('user')
    Comment.objects.get(movie_name=movie, user_name=user).delete()
    return redirect('/movie/?movie_name=%s' % (movie))

def modify_comment(request): #wrong
    movie =  request.GET.get('movie_name')
    user = request.GET.get('user')
    new_grade = request.GET.get('score')
    new_comment = request.GET.get('comment')
    q = Comment.objects.get(movie_name=movie, user_name=user)
    q.update(comment=new_comment,grade=new_grade)
    return redirect('/movie/?movie_name=%s' % (movie))