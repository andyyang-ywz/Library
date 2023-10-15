from django.db.models import Q
from Library.models import Book, Transaction
from Seller.models import Seller
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
      cart = []
      for x in cart_arr:
         cart.append(Book.objects.get(pk=x))
      page_context['cart'] = cart

   try:
      Seller.objects.get(user=request.user)
      page_context['is_seller'] = True
   except:
      page_context['is_seller'] = False
      
   return page_context