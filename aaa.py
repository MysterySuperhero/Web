# -*- coding: utf-8 -*-

from ask_nazarkov.models import Question
from django.contrib.auth.models import User

User.objects.all()

u = User.objects.get(id=1)

for i in 'abcdef':
	Question(title=u'Как построить Технопарк', content=u'Чё-то не получается.', author=u)	
	Question(title=u'Как построить Технопарк', content=u'Чё-то не получается.', author=u).save()