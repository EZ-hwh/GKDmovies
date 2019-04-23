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
    p = request.GET.get('state')

    if not q:
        return render(request, 'Frontpage.html', {})
		
    if p == 'all' or not p:
        person_list = Person.objects.filter(name__contains=q).order_by('name')
        movie_list = Movie.objects.filter(movie_name__contains=q).order_by('movie_name')
        return render(request, 'results.html', {'person_list': person_list , 'movie_list': movie_list})

    if p == 'person' :
        person_list = Person.objects.filter(name__contains=q).order_by('name')
        return render(request, 'results.html', {'person_list': person_list})
    
    if p == 'movie' :
        movie_list = Movie.objects.filter(movie_name__contains=q).order_by('movie_name')
        return render(request, 'results.html', {'movie_list': movie_list})
  
	
def person(request):
    q = request.GET.get('person_name')
    person = Person.objects.get(person_name=q)    
    movie_d = Direct.objects.filter(person_name=q)
    movie_a = Play.objects.filter(person_name=q)
    return render(request, 'person.html', {'person': person, 'movie_d': movie_d, 'movie_a':movie_a})

def movie(request): 
    q = request.GET.get('movie_name')
    p = request.session.get('user_name',None)
    login = request.session.get('login',None)   
    movie = Movie.objects.get(movie_name=q)
    user = User.objects.get(user_name=p)
    director = Direct.objects.filter(movie_name=q)
    actor = Play.objects.filter(movie_name=q)
    comment = Comment.objects.filter(movie_name=q)
    
    if not login:
        return render(request, 'movie.html', {'actor': actor, 'director': director, 'movie': movie, 'comment': comment})
        
    if Comment.objects.filter(user_name=user,movie_name=movie) : 
        uc = Comment.objects.get(user_name=user,movie_name=movie)
        return render(request, 'movie.html', {'actor': actor, 'director': director, 'movie': movie, 'comment': comment, 'uc': uc})
    
    n_exist = True   
    return render(request, 'movie.html', {'actor': actor, 'director': director, 'movie': movie, 'comment': comment, 'n_exist': n_exist})  
    

def user(request):
    q = request.session['user_name']
    user = User.objects.get(user_name=q)
    return render(request, 'user.html', {'user': user})    
 
def person_all(request):
    person_list = Person.objects.all()
    return render(request, 'results.html', {'person_list': person_list})
	
def movie_all(request):
    movie_list = Movie.objects.all()
    return render(request, 'results.html', {'movie_list': movie_list})

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

def add_comment(request): 
    q = request.GET.get('movie_name')
    p = request.session.get('user_name',None)
    grade = request.GET.get('score')
    comment = request.GET.get('comment')
      
    if not comment :
        return redirect('/movie/?movie_name=%s' % (movie.movie_name)) 
    
    movie = Movie.objects.get(movie_name=q)   
    user = User.objects.get(user_name=p)
    Comment.objects.create(movie_name=movie,user_name=user,grade=grade,comment=comment)
    
    return redirect('/movie/?movie_name=%s' % (movie.movie_name)) 
    
 
def delete_comment(request): #wrong  
    q = request.GET.get('movie_name')
    p = request.session.get('user_name',None)
    movie = Movie.objects.get(movie_name=q)   
    user = User.objects.get(user_name=p)
    Comment.objects.get(movie_name=movie, user_name=user).delete()
    return redirect('/movie/?movie_name=%s' % (movie.movie_name))

def modify_comment(request): #wrong
    q = request.GET.get('movie_name')
    p = request.session.get('user_name',None)
    movie = Movie.objects.get(movie_name=q)   
    user = User.objects.get(user_name=p)
    new_grade = request.GET.get('score')
    new_comment = request.GET.get('comment')
    q = Comment.objects.get(movie_name=movie, user_name=user)
    q.comment = new_comment
    q.grade = new_grade
    q.save()
    return redirect('/movie/?movie_name=%s' % (movie.movie_name))