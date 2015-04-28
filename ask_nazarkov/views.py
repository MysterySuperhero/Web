# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from django.core.paginator import Paginator, EmptyPage
from models import Question, Answer, Tag, User, UserProfile


def pagination(all_objects, request):
  paginator = Paginator(all_objects, 10)
  page = 1
	
  if request.GET.get('page'):
    page = int(request.GET.get('page'))
  if page < 1:
    page = 1

  try:
    objects = paginator.page(page)
  except EmptyPage:
    objects = paginator.page(paginator.num_pages)
	
  return objects	

def base(request):
	return render(request, 'base.html')

def index(request):
  url = request.path
  order = 'date'
  tag = 'none'
  if request.GET.get('order') == 'rating':
    order = 'rating'

  url = url + "?order=" + order
  questions_all = Question.objects.order_by('-' + order)

  questions = pagination(questions_all, request)
  penult_page = questions.paginator.num_pages - 1
  parameters = {
    'url': url,
    'questions_all' : questions,
    'penult_page': penult_page,
  }
  return render(request, 'index.html', parameters)

def tag(request, tagname):
  url = request.path

  tag = Tag.objects.get( name = tagname )
  question_list = tag.question_set.order_by('-rating')
  
  questions = pagination(question_list, request)

  penult_page = questions.paginator.num_pages - 1
  params = {
    'questions_all':questions,
    'tag':tag,
    'penult_page': penult_page,
    'url':url
  }
  return render(request, 'tag.html', params)

def new_question(request):
	return render(request, 'new_question.html')

def register(request):
	return render(request, 'register.html')

def login(request):
	return render(request, 'login.html')

def question(request):  
  question_id = 1;
  page = 1;
  if request.GET.get('id'):
    question_id = int(request.GET.get('id'))
  
  if question_id < 1:
		question_id = 1
  
  q = Question.objects.get(id = question_id)
  
  ans = q.answers.order_by('-date').all()

  answers = pagination(ans, request) 	
    
  url = "/question?id="+str(question_id)
  user = User.objects.get(id = q.author_id)
  penult_page = answers.paginator.num_pages - 1
  return render(request, 'question.html',
  	{
	  	'question': q,
	   	'answers': answers,
	   	'url' : url,
	   	'user' : user,
	   	'penult_page' : penult_page,
  	})


def getparameters(request):
  return render(request, 'getparameters.html')

def search(request):
    if request.GET.get('q'):
        message = 'You searched for: %s' %request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def helloworld(request):
    return render(request, 'helloworld.html')

