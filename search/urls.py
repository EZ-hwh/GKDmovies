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
    path('<int:question_id>/user/', views.User, name='results'),
]