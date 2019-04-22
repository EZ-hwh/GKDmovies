#edit:-*coding=utf-8*-
from django.db import models
import datetime 
from django.utils import timezone

class Actor(models.Model):
    actor_name = models.CharField(max_length=50, primary_key=True)
    actor_date = models.CharField(max_length=50,blank=True,null=True)
    constellation = models.TextField(blank=True)
    birthplace = models.TextField(blank=True)
    occupation = models.TextField(blank=True)
    website = models.TextField(blank=True)
    actor_intro = models.TextField()
    actor_photo = models.ImageField(default="actorset/no_img.jpg",upload_to="actorset/")
    gender_status = (
        ('m', 'male'),
        ('f', 'female'),
    )
	
    actor_gender = models.CharField(max_length=1, choices=gender_status, blank=True)
	
    def __str__(self):
        return self.actor_name	
		

class Director(models.Model):
    director_name = models.CharField(max_length=50, primary_key=True)
    director_date = models.CharField(max_length=50,blank=True,null=True)
    constellation = models.TextField(blank=True)
    birthplace = models.TextField(blank=True)
    occupation = models.TextField(blank=True)
    website = models.TextField(blank=True)
    director_intro = models.TextField()
    director_photo = models.ImageField(default="directorset/no_img.jpg",upload_to="directorset/")
    gender_status = (
		('m', 'male'),
		('f', 'female'),
	)
	
    director_gender = models.CharField(max_length=1, choices=gender_status, blank=True)

    def __str__(self):
        return self.director_name	
		
	
class Movie(models.Model):
    movie_name = models.CharField(max_length=50, primary_key=True)
    movie_date = models.CharField(max_length=50,blank=True,null=True)
    synopsis = models.TextField()
    type = models.TextField()
    place = models.TextField()
    language = models.TextField()
    length = models.TextField()
    rename = models.TextField()
    
    movie_photo = models.ImageField(default="movieset/no_img.jpg",upload_to="movieset/")
	
    def __str__(self):
        return self.movie_name	
	
	
class User(models.Model):
	user_name = models.CharField(max_length=50, primary_key=True)
	password = models.CharField(max_length=50)
	signature = models.TextField()
	user_photo = models.ImageField(default="userset/no_img.jpg",upload_to="userset/")
	
	def __str__(self):
		return self.user_name	
        
class Direct(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director_name = models.ForeignKey(Director, on_delete=models.CASCADE)
	
    def __str__(self):
        return self.movie_name + '-' + self.director_name	
	
class Play(models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	actor_name = models.ForeignKey(Actor, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.movie_name + '-' + self.actor_name	
	
	
class Label(models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	label = models.CharField(max_length=50)
	
	def __str__(self):
		return self.movie_name	

	
class Comment(models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField()
	grade = models.IntegerField(blank=True)
	
	def __str__(self):
		return self.movie_name + '-' + self.user_name

class Skim(models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	skim_date = models.DateField()
	
	def __str__(self):
		return self.movie_name + '-' + self.user_name
	
	
	