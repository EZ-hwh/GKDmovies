from django.db import models
import datetime 
from django.utils import timezone

class Actor(models.Model):
	actor_name = models.CharField(max_length=50, primary_key=True)
	actor_intro = models.TextField()
	
	gender_status = (
		('m', 'male'),
		('f', 'female'),
	)
	
	actor_gender = models.CharField(max_length=1, choices=gender_status, blank=True)
	
	def __str__(self):
		return self.actor_name	
		

class Director(models.Model):
	director_name = models.CharField(max_length=50, primary_key=True)
	director_intro = models.TextField()
	
	gender_status = (
		('m', 'male'),
		('f', 'female'),
	)
	
	director_gender = models.CharField(max_length=1, choices=gender_status, blank=True)

	def __str__(self):
		return self.director_name	
		
	
class Movie(models.Model):
	movie_name = models.CharField(max_length=50, primary_key=True)
	director_name = models.ForeignKey(Director, on_delete=models.CASCADE)
	date = models.DateField(blank=True)
	synopsis = models.TextField()
	photo = models.ImageField()
	
	def __str__(self):
		return self.movie_name	
	
	
class User(models.Model):
	user_name = models.CharField(max_length=50, primary_key=True)
	password = models.CharField(max_length=50)
	signature = models.TextField()
	
	def __str__(self):
		return self.user_name	
	
	
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

	
class Comment(Models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField()
	grade = models.IntegerField(blank=True)
	
	def __str__(self):
		return self.movie_name + '-' + self.user_name
	
	
class Friend(Models.Model):
	user_name1 = models.ForeignKey(User, on_delete=models.CASCADE)
	user_name2 = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.user_name1 + '-' + self.user_name2
	
	
class Skim(Models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	skim_date = models.DateField()
	
	def __str__(self):
		return self.movie_name + '-' + self.user_name
	
	
	