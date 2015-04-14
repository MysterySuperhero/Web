from django.db import models
from django.contrib.auth.models import User
import datetime

# class User(object):
# 	username  = models.CharField(max_length = 25)
# 	email = models.EmailField(max_length = 100)
# 	password = models.CharField(max_length = 60)
# 	avatar = models.ImageField()


class Question(models.Model):
  title = models.CharField(max_length = 200)
  content = models.TextField()
  author = models.ForeignKey(User)
  date = models.DateTimeField(default = datetime.datetime.now)
  tags = models.ManyToManyField('Tag')
  rating = models.IntegerField(null=False, default=0)	

  def _unicode_(self):
  	return self.title
		

class Answer(models.Model):
  question = models.ForeignKey('Question')
  content = models.TextField()
  author = models.ForeignKey(User)
  date = models.DateTimeField(auto_now_add = True)


class Tag(models.Model):
	name = models.CharField(max_length = 100)
		
		