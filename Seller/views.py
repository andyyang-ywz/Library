from django.shortcuts import render
from django.views.generic import CreateView
from .forms import NewProductForm

# Create your views here.
class AddProductPage(CreateView):
   template_name = 'seller/add_product.html'
   form_class = NewProductForm

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      print(page_context)
      return page_context