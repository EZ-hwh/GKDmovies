from django.http import HttpResponse,Http404
from .models import *
from django.shortcuts import render,get_object_or_404

# Create your views here.

def Frontpage(request):
    return render(request, "Frontpage.html",{})

def search(request):
    q = request.GET.get('index')
    p = request.GET.get('person')

    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'errors.html', {'error_msg': error_msg})
		
    if p == 'all' or not p:
        actor_list = Actor.objects.filter(actor_name__contains=q)
        movie_list = Movie.objects.filter(movie_name__contains=q)
        director_list = Director.objects.filter(director_name__contains=q)
        return render(request, 'results.html', {'error_msg': error_msg, 'actor_list': actor_list , 'movie_list': movie_list , 'director_list': director_list})

    if p == 'actor' :
        actor_list = Actor.objects.filter(actor_name__contains=q)
        return render(request, 'results.html', {'error_msg': error_msg, 'actor_list': actor_list})
    
    if p == 'movie' :
        movie_list = Movie.objects.filter(movie_name__contains=q)
        return render(request, 'results.html', {'error_msg': error_msg, 'movie_list': movie_list})

    if p == 'director' :
        director_list = Director.objects.filter(director_name__contains=q)
        return render(request, 'results.html', {'error_msg': error_msg, 'director_list': director_list})
	
def actor(request):
    q = request.GET.get('actor_name')
    actor = Actor.objects.get(actor_name=q)
    movie = Play.objects.filter(actor_name=q)
    return render(request, 'actor.html', {'actor': actor, 'movie': movie})

def movie(request):
    q = request.GET.get('movie_name')
    movie = Movie.objects.get(movie_name=q)
    actor = Play.objects.filter(movie_name=q)
    return render(request, 'movie.html', {'actor': actor, 'movie': movie})

def director(request):
    q = request.GET.get('director_name')
    director = Director.objects.get(director_name=q)
    movie = Movie.objects.filter(director_name=q)
    return render(request, 'director.html', {'director': director, 'movie': movie})

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
    
def register(request):
    return render(request, 'register.html', {})
    