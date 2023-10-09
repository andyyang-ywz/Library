from django.db.models import Q
from .models import Category
from User.models import UserDetail
from Library.models import Transaction

def context_processor(request):
   return {
      'fictional_categories': Category.objects.filter(is_fictional=True).all(),
      'nonfictional_categories': Category.objects.filter(is_fictional=False).all(),
      'transaction_history': Transaction.objects.filter(Q(arrival_status="Book Arrived!") & ~Q(arrive_date=None))
   }