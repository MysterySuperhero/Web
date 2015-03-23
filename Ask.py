from cgi import parse_qs,escape

def application(environ, start_response):
  start_response('200 OK',[('Content-Type','text/html')])
  res="""
    <html>
      <head>
        <title>Get and Post parameters</title>
      </head>
      <body>
  """
  res+="<h1>Hello cruel world!</h1>\n"

  #GET form
  res+="""<h2>GET</h2>\n<ol> 
    <form action="" method="get">
      <input type="text" name="name" />
      <input type="text" name="surname" />
      <input type="submit" value="Send"/>
    </form>
  """

  #parsim query string, polychaem parametry
  d=parse_qs(environ['QUERY_STRING'])
  for k in d:
    res += "<li>%s = " % k
    for v in d[k]:
      res += "%s</li>" % v
  
  # analogichno
  res+="""</ol>\n<h2>POST</h2>\n<ol>
    <form action="" method="POST">
      <input type="text" name="name" />
      <input type="text" name="surname" />
      <input type="submit" value="Send"/>
    </form>
  """
  p=parse_qs(environ['wsgi.input'].readline())
  for name in p:
    res += "<li>%s = " % name
    for val in p[name]:
      res += "%s<br></li>" % val

  res += """</ol>
      </body>
    </html>
  """
  return res
