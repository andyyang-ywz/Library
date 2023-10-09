from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, TemplateView, View
from .forms import NewProductForm, NewSellerForm
from .models import Seller
from Library.models import Book, BookPicture

# Create your views here.
class AddProductPage(CreateView):
   template_name = 'seller/add_product.html'
   form_class = NewProductForm

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      return page_context

   def post(self, request, *args, **kwargs):
      form = NewProductForm(request.POST)
      if form.is_valid():
         form.save()

         seller_account = Seller.objects.get(user_id=request.user.id)
         if not seller_account.account_active:
            seller_account.account_active = True
            seller_account.save()

         messages.success(request, 'Your new product has been successfully uploaded into the database.')

         return redirect('Seller:upload_image')
      return super().post(self, request)


class OpenSellerAccount(CreateView):
   template_name = 'seller/open_seller_account.html'
   model = Seller
   form_class = NewSellerForm

   def post(self, request, *args, **kwargs):
      form = NewSellerForm(request.POST, request.FILES)
      if form.is_valid():
         store_name = form.cleaned_data['store_name']
         image      = form.cleaned_data['image']
         desc       = form.cleaned_data['desc']
         location   = form.cleaned_data['location']

         new_seller_account = Seller(
            store_name = store_name,
            image      = image,
            desc       = desc,
            location   = location,
            user       = request.user,
         )
         new_seller_account.save()

         messages.success(request, 'You have made your seller account. But before we publicize you account, please upload your first product.')

         return redirect('Seller:add_product')
      return super().post(self, request)


class ProductImageUpload(View):
   template_name = 'seller/product_image_form.html'

   def get(self, request, *args, **kwargs):
      book = Book.objects.get(id=kwargs['book_id'])
      return render(request, self.template_name, {
         'book_name': book.name
      })
   
   def post(self, request, *args, **kwargs):
      book = Book.objects.get(id=kwargs['book_id'])
      for x in range(1, len(request.FILES) + 1):
         if x == 1:
            new_picture = BookPicture(image=request.FILES['image' + str(x)], book=book, is_main_image=1)
         else:
            new_picture = BookPicture(image=request.FILES['image' + str(x)], book=book)

         new_picture.save()

      if len(request.FILES) > 0:
         messages.success(request, 'Congratulation!! Your product is successfully publisized. Time to wait for buyers.')
         return render(request, self.template_name)


      messages.error(request, 'Please upload at least 1 image!!')
      return render(request, self.template_name, {
         'book_name': book.name
      })
