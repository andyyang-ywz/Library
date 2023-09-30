from django import template

register = template.Library()

@register.filter
def divide(value):
   try:
      return int(value) // 2
   except:
      return None