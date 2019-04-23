#edit:-*coding=utf-8*-
from django.db import models
import datetime 
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    birthdate = models.CharField(max_length=50,blank=True,null=True)
    constellation = models.TextField(blank=True,null=True)
    birthplace = models.TextField(blank=True,null=True)
    occupation = models.TextField(blank=True,null=True)
    intro = models.TextField()
    photo = models.ImageField(default="personset/no_img.jpg",upload_to="personset/")
    gender_status = (
        ('m', 'male'),
        ('f', 'female'),
    )
	
    gender = models.CharField(max_length=1, choices=gender_status, blank=True)
	
		
'''
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
'''		
	
class Movie(models.Model):
    movie_name = models.CharField(max_length=50, primary_key=True)
    movie_date = models.CharField(max_length=50,blank=True,null=True)
    intro = models.TextField(blank=True,null=True)
    type = models.TextField(blank=True,null=True)
    place = models.TextField(blank=True,null=True)
    language = models.TextField(blank=True,null=True)
    length = models.TextField(blank=True,null=True)
    rename = models.TextField(blank=True,null=True)
    
    photo = models.ImageField(default="movieset/no_img.jpg",upload_to="movieset/")
	
	
	
class User(models.Model):
	user_name = models.CharField(max_length=50, primary_key=True)
	password = models.CharField(max_length=50)
	signature = models.TextField(blank=True,null=True)
	user_photo = models.ImageField(default="userset/no_img.jpg",upload_to="userset/")
	
        
class Direct(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director_name = models.ForeignKey(Person, on_delete=models.CASCADE)
	
	
class Play(models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	actor_name = models.ForeignKey(Person, on_delete=models.CASCADE)
	
	
'''	
class Label(models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	label = models.CharField(max_length=50)
	
	def __str__(self):
		return self.movie_name	
'''
	
class Comment(models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField(blank=True,null=True)
	grade = models.IntegerField(blank=True)
	

'''
class Skim(models.Model):
	movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	skim_date = models.DateField()
	
	def __str__(self):
		return self.movie_name + '-' + self.user_name
'''	
	