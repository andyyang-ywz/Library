from .models import Category
from User.models import UserDetail

def context_processor(request):
   return {
      'fictional_categories': Category.objects.filter(is_fictional=True).all(),
      'nonfictional_categories': Category.objects.filter(is_fictional=False).all(),
   }