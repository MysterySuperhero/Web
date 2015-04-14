# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
import datetime


def base(request):
	return render(request, 'base.html')

questions = [

	{'title': u'Как построить лунапарк?', 'content': u'читай тут ->', 'tags':['moon', 'howto'], 'created': datetime.datetime.now()},
	{'title': u'Как построить Технопарк?', 'content': u'читай тут ->', 'tags':['techno', 'howto'], 'created': datetime.datetime.now()},
	{'title': u'Как построить аквапарк?', 'content': u'читай тут ->', 'tags':['aquas', 'howto'], 'created': datetime.datetime.now()},
]

def index(request):
	context = {
		# 'questions': Questions.objects.all()
		'questions': questions
	}
	return render(request, 'index.html', context)

def new_question(request):
	return render(request, 'new_question.html')

def register(request):
	return render(request, 'register.html')

def login(request):
	return render(request, 'login.html')

def question(request):  # ,pk
	# data = {
	# 	'pk' = int(pk)
	# }
	return render(request, 'question.html')

def getparameters(request):
	return render(request, 'getparameters.html')

# def search(request):
#     if request.GET.get('q'):
#         message = 'You searched for: %s' %request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

def helloworld(request):
    return render(request, 'helloworld.html')

