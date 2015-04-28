import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")
django.setup()

from django.core.management.base import BaseCommand, CommandError

from django.db import models
from django.contrib.auth.models import User
from ask_nazarkov.models import Question, Answer, Tag

import names

class Command(BaseCommand):

	def create_new_user():
	    username = names.get_full_name(gender='male')
	    email = username.replace(' ', '_') + "@mail.ru"
	    password = "password"

	    new_user = User.objects.create_new_user(username=username, email=email, password=password)
	    new_user
	    new_user.save()

	    # author = UserProperties.objects.create(
	    #     user=new_user,
	    #     filename="ex1.jpg",
	    #     nickname=username[:20],
	    # )
	    return new_user

	def handle(self, **options):
   	 username = names.get_full_name(gender='male')
	 email = username.replace(' ', '_') + "@mail.ru"
	 password = "password"

	 new_user = User.objects.handle(username=username, email=email, password=password)
	 new_user
	 new_user.save()



