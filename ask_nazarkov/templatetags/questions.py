from django import template
  
register = template.Library()

@register.inclusion_tag("questions.html")
def questions(question):
  return {'question' : question}
