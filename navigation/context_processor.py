from django.db.models import Q
from User.models import UserDetail
from Library.models import Book, Transaction
from .models import Category
import json

def context_processor(request):
   if request.user.is_authenticated:
      transaction_history = Transaction.objects.filter(Q(arrival_status="Book Arrived!") & ~Q(arrive_date=None) & Q(user=request.user))
   else:
      transaction_history = {}

   page_context = {
      'fictional_categories': Category.objects.filter(is_fictional=True).all(),
      'nonfictional_categories': Category.objects.filter(is_fictional=False).all(),
      'transaction_history': transaction_history,
      'request': request
   }

   if 'cart' in request.COOKIES:
      cart_arr = json.loads(request.COOKIES['cart'])
      print(cart_arr)
      cart = []
      for x in cart_arr:
         cart.append(Book.objects.get(pk=x))
      page_context['cart'] = cart

      
   return page_context