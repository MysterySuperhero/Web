import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")
django.setup()

from django.db import models
from django.contrib.auth.models import User
from ask_nazarkov.models import Question, Answer, Tag, UserProfile

import names
import random
import string

def create_new_user():
	username = names.get_full_name(gender='male')
	username = username + str(random.randrange(10000)) + random.choice(string.letters)
	email = username.replace(' ', '_') + "@mail.ru"
	password = "password"

	new_user = User.objects.create(
		username = username, 
		email = email, 
		password= "password",
	)
	userprofile = UserProfile.objects.create(
		user_id = new_user.id, 
		rating = 0,
	)
	new_user.save()
	userprofile.save()
	print userprofile.id

	return userprofile

def create_tags():
	tagname = names.get_first_name(gender = None)
	tagname = tagname + str(random.randrange(10000)) + random.choice(string.letters)
	new_tag = Tag.objects.create(name = tagname)
	new_tag.save()

def create_new_question( user ):
	x = random.randint(0, 50)
	
	text = "How to "
	for y in range(0, x):
		text = text + "".join( [random.choice(string.letters) for i in xrange(10)] )
		text = text + " "
		
	text = text[:text.rfind(" ") - 1] + '?'

	title_text = "".join( [random.choice(string.letters) for i in xrange(10)] )
	question = Question.objects.create(
		author = user,
		title = title_text,
		content = text,	
		rating = random.randint(0, 200), 
	)
	question.tags.add(Tag.objects.get(id = random.randint(11, 10010)))
	
	print question.id

	for ii in range(0, 3):
		x = random.randint(0, 50)
		text = "ANSWER: "
		for y in range(0, x):
			text = text + "".join( [random.choice(string.letters) for i in xrange(10)] )
			text = text + " "
		text = text[:text.rfind(" ") - 1] + '.'
		question.answers.add(Answer.objects.create(
				content = text,
				author = user,
			)
		)

def add():
	for i in range(1, 10001):
		create_new_user()
	# 	create_tags()
	for i in range(1, 100001):
		user = UserProfile.objects.get( id = random.randint(50, 1049) )
		create_new_question( user )


def azaza():
	print Question.objects.get(id = 1).tags.name

def add_more_questions():
	for i in range(1, 40000):
		user = UserProfile.objects.get( id = random.randint(1, 10000) )
		create_new_question( user )

def add_moar_tags():
	for i in range(1, 100000):
		question = Question.objects.get(id = i)
		question.tags.add(Tag.objects.get(id = random.randint(1, 500)))
		question.tags.add(Tag.objects.get(id = random.randint(1, 500)))
		question.tags.add(Tag.objects.get(id = random.randint(1, 500)))

add_moar_tags()
