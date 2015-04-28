from django.db import models
from django.contrib.auth.models import AbstractUser, User
import datetime

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	rating = models.IntegerField()
	avatar = models.ImageField()

class Question(models.Model):
  title = models.CharField(max_length = 200)
  content = models.TextField()
  author = models.ForeignKey(UserProfile)
  date = models.DateTimeField(default = datetime.datetime.now)
  tags = models.ManyToManyField('Tag')
  answers = models.ManyToManyField('Answer')
  rating = models.IntegerField( null=False, default=0 )	

def _unicode_(self):
  return self.title
		
class Answer(models.Model):
  content = models.TextField()
  author = models.ForeignKey(UserProfile)
  date = models.DateTimeField(default = datetime.datetime.now)


class Tag(models.Model):
	name = models.CharField(max_length = 100)
		