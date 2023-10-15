from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, TemplateView, View, UpdateView
from django.utils import timezone
from Library.models import Transaction, Book, BookPicture
from .forms import NewProductForm, SellerDataForm
from .models import Seller

# Create your views here.
class AddProductPage(CreateView):
   template_name = 'seller/add_product.html'
   form_class = NewProductForm

   def post(self, request, *args, **kwargs):      
      form = NewProductForm(request.POST)
      if form.is_valid():
         form.save()

         seller_account = Seller.objects.get(user_id=request.user.id)
         if not seller_account.account_active:
            seller_account.account_active = True
            seller_account.save()

         messages.success(request, 'Your new product has been successfully uploaded into the database.')

         return redirect('Seller:upload_image', book_id=form.instance.id)
      return super().post(self, request)


class OpenSellerAccount(CreateView):
   template_name = 'seller/open_seller_account.html'
   model = Seller
   form_class = SellerDataForm

   def post(self, request, *args, **kwargs):
      form = SellerDataForm(request.POST, request.FILES)
      if form.is_valid():
         store_name   = form.cleaned_data['store_name']
         phone_number = form.cleaned_data['phone_number']
         image        = form.cleaned_data['image']
         desc         = form.cleaned_data['desc']
         location     = form.cleaned_data['location']

         new_seller_account = Seller(
            store_name   = store_name,
            phone_number = phone_number,
            image        = image,
            desc         = desc,
            location     = location,
            user         = request.user,
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

      if len(request.FILES) > 0:
      
         current_images = BookPicture.objects.filter(book=book)
         for image in current_images:
            image.delete()
         
         for x in range(1, len(request.FILES) + 1):
            if x == 1:
               new_picture = BookPicture(image=request.FILES['image' + str(x)], book=book, is_main_image=1)
            else:
               new_picture = BookPicture(image=request.FILES['image' + str(x)], book=book)

            if book.book_activated == 0:
               book.book_activated = 1
               book.save()

            new_picture.save()

            messages.success(request, 'Congratulation!! Your product is successfully publisized. Time to wait for buyers.')
            return redirect('Library:book_detail', pk=book.id)


      messages.error(request, 'Please upload at least 1 image!!')
      return render(request, self.template_name, {
         'book_name': book.name
      })


class SellerAccountPage(TemplateView):
   template_name = 'seller/account.html'

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      seller = Seller.objects.get(pk=kwargs['seller_id'])
      page_context['seller'] = seller
      page_context['books'] = Book.objects.filter(book_activated=1, seller=seller).order_by('-id')
      return page_context


class EditSellerAccountPage(UpdateView):
   template_name = 'seller/open_seller_account.html'
   model = Seller
   form_class = SellerDataForm

   def get(self, request, *args, **kwargs):
      if kwargs['pk'] != request.user.id:
         return render(request, self.template_name, {
            'form': self.form_class(instance=Seller.objects.get(pk=request.user))
         })

      return redirect('Seller:edit_seller_account', seller_id=request.user.id)


   def get_success_url(self):
      messages.success(self.request, 'Your seller account has been updated!')
      return reverse("Seller:account", kwargs={'seller_id': self.request.user.id})



class EditProductPage(UpdateView):
   template_name = 'seller/add_product.html'
   model = Book
   form_class = NewProductForm

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      page_context['book_id'] = page_context['book'].id
      return page_context

   def form_valid(self, form):
      object_id = self.object.id
      return HttpResponseRedirect(self.get_success_url(object_id))

   def get_success_url(self, book_id):
      print(book_id)
      return reverse_lazy("Library:book_detail", kwargs={'pk': book_id})


class CustomerOrderPage(TemplateView):
   template_name = 'seller/customer_order.html'

   def get(self, request, *args, **kwargs):
      seller = Seller.objects.get(pk=request.user.id)
      
      return render(request, self.template_name, {
         'orders': Transaction.objects.filter(seller=seller, arrive_date=None).order_by('-id')
      })

def update_track(request, order_id):
   order_step = ["Waiting For Confirmations", "Currently On Shipping", "Book Arrived!"]
   order = Transaction.objects.get(pk=order_id)
   current_index = order_step.index(order.arrival_status)

   if current_index == 2:
      messages.success(request, 'Order already arrived!! No need to update it again!')
      return redirect('Seller:customer_orders')

   order.arrival_status = order_step[current_index + 1]
   if current_index == 1:
      order.arrive_date = timezone.now()

   order.save()

   messages.success(request, 'Order already updated!!')
   return redirect('Seller:customer_orders')

   
