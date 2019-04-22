from django.urls import path
from . import views
import re

app_name='search'
urlpatterns = [
    path('', views.Frontpage, name='frontpage'),
    path('search/', views.search, name='search'),
    path('actor/', views.actor, name='actor'),
	path('movie/', views.movie, name='movie'),
    path('director/', views.director, name='director'),
	path('actor_all/', views.actor_all, name='actor_all'),
	path('movie_all/', views.movie_all, name='movie_all'),
    path('director_all/', views.director_all, name='director_all'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('user/', views.user, name='user'),
    path('add_user/', views.add_user, name='add_user'),
    path('check/', views.check, name='check'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
    path('modify_comment/', views.modify_comment, name='modify_comment'),
]