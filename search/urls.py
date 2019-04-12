from django.urls import path
from . import views

app_name='search'
urlpatterns = [
    path('', views.Frontpage, name='frontpage'),
    # ex: /polls/
    path('actor/', views.Actor, name='index'),
    # ex: /polls/5/
    path('director/', views.Director, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/user/', views.User, name='results'),
]