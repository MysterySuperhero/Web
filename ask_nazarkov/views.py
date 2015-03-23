from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template

# def getparameters(request):
#   html="""
# <!DOCTYPE html>
# <html>
#  <body>
#   <h1>View parameters</h1>
#    <h2>GET</h2>
#    <form action="" method="get">
#       <input type="text" name="name" />
#       <input type="text" name="surname" />
#       <input type="submit" value="Send"/>
#     </form>
#     <ul>
# """
#   for r in request.GET:
#     html+="<li>"+r+"="+request.GET.get(r,'')+"</li>"
#   html+="""
#     </ul>
#    <h2>POST</h2>
#    <form action="" method="post">
#       <input type="text" name="name" />
#       <input type="text" name="surname" />
#       <input type="submit" value="Send"/>
#     </form>
#     <ul>"""
#   for r in request.POST:
#     html+="<li>"+r+"="+request.POST.get(r,'')+"</li>"
#   html+="""
#     </ul>
#  </body>
# </html>
# """
#   return HttpResponse(html)

def getparameters(request):
	return render(request, 'getparameters.html')

def search(request):
    if request.GET.get('q'):
        message = 'You searched for: %r' %request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def helloworld(request):
    return render(request, 'helloworld.html')

