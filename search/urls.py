from django.urls import path
from . import views
import re

app_name='search'
urlpatterns = [
    path('', views.Frontpage, name='frontpage'),
    path('search/', views.search, name='search'),
    path('director/', views.Director, name='detail'),
    path('<int:question_id>/user/', views.User, name='results'),
]