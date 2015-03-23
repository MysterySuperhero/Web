from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template

def helloworld(request):
    return render(request, 'helloworld.html')
