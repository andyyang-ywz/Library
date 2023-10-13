from django import template
from Library.models import BookPicture
import json

register = template.Library()

@register.filter
def divide(value):
   try:
      return int(value) // 2
   except:
      return None

@register.filter
def find_main_image(value):
   return BookPicture.objects.filter(is_main_image=1, book=value).first()

@register.filter
def in_cart(value, cart):
   cart_arr = json.loads(cart)
   return value in cart_arr
