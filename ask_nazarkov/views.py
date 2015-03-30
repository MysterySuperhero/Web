from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template

def base(request):
	return render(request, 'base.html')

def index(request):
	return render(request, 'index.html')

def new_question(request):
	return render(request, 'new_question.html')

def register(request):
	return render(request, 'register.html')

def login(request):
	return render(request, 'login.html')

def question(request):
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

