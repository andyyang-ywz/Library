from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView, FormView, View
from django.contrib import messages
from django.http import HttpResponse
from navigation.models import Category
from .models import Book, BookPicture, Transaction
from .forms import TransactionForm, FeedbackReportForm
import json


# Create your views here.
class MainIndex(TemplateView):
   template_name = 'library/index.html'

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      page_context['books'] = Book.objects.all().order_by('-id')
      return page_context

class BookDetailPage(DetailView):
   template_name = 'library/book_detail.html'
   model = Book

   def get_recommended_book(self, book):
      query_1 = Book.objects.\
               filter(category=book.category).\
               order_by('-id').\
               exclude(id=book.id)[:10]

      additional_book = 10 - len(query_1)
      
      query_2 = Book.objects.\
               exclude(category=book.category).\
               order_by('-id')[:additional_book]

      return query_1.union(query_2)

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      book = page_context['book']
      page_context['books'] = self.get_recommended_book(book)
      page_context['book_pictures'] = BookPicture.objects.filter(book=book).order_by('-is_main_image')

      page_context['details'] = [
         {'title': 'Author'        , 'value': book.author},
         {'title': 'Category'      , 'value': book.category.name},
         {'title': 'Publisher'     , 'value': book.publisher},
         {'title': 'Total Page'    , 'value': book.total_pages},
         {'title': 'Total Chapters', 'value': book.total_chapters},
         {'title': 'Publish Year'  , 'value': book.publish_year},
         {'title': 'Weight'        , 'value': str(book.weight) + ' gram'},
         {'title': 'Size'          , 'value': book.size + ' cm'},
         {'title': 'Serial Number' , 'value': book.serial_number}
      ]
      return page_context



class PurchasePage(FormView):
   template_name = 'library/purchase.html'
   form = TransactionForm

   def get(self, request, *args, **kwargs):
      form_initial = {'shipment_method': 'Normal Shipment'}
      if 'saved_address' in request.COOKIES:
         form_initial['address'] = request.COOKIES['saved_address']
      return render(request, self.template_name, {
         'form': TransactionForm(initial=form_initial),
         'book': Book.objects.get(id=kwargs['book_id'])
      })
   
   def post(self, request, *args, **kwargs):
      validated_data = {
         'address'        : request.POST['address'],
         'shipment_method': request.POST['shipment_method'],
         'payment_method' : request.POST['payment_method']
      }
      form = TransactionForm(validated_data)
      if form.is_valid():
         messages.success(request, 'Order Fulfilled, please enter your payment code.')
         return redirect(
            'Library:payment_process',
            address         = form.cleaned_data['address'],
            shipment_method = form.cleaned_data['shipment_method'],
            payment_method  = form.cleaned_data['payment_method'],
            book_id         = request.POST['book_id']
         )
      
      return render(request, self.template_name, {
         'form': form,
         'book': Book.objects.get(id=kwargs['book_id'])
      })



class PaymentProcessPage(FormView):
   template_name = 'library/payment.html'

   def get(self, request, *args, **kwargs):
      page_context = kwargs
      page_context['payment_logo_img'] = kwargs['payment_method'].lower() + '.png'
      
      return render(request, self.template_name, page_context)

   def post(self, request, *args, **kwargs):
      available_payment_method = ['BCA', 'Paypal', 'Ovo']
      avaialbel_shipment_method = ['Normal Shipment', 'Fast Shipment', 'Slow Shipment']
      if kwargs['payment_method'] in available_payment_method and kwargs['shipment_method'] in avaialbel_shipment_method:
         book = Book.objects.get(pk=kwargs['book_id'])

         new_transaction = Transaction(
            address         = kwargs['address'],
            shipment_method = kwargs['shipment_method'],
            payment_method  = kwargs['payment_method'],
            user            = request.user,
            seller          = book.seller,
            book            = book,
         )
         new_transaction.save()
         
         messages.success(request, 'The book has been purchased. Your book will arive soon!!!')
         return redirect('Library:main')
      
      messages.error(request, 'Something went wrong! Please try again..')
      return self.get(request, *args, **kwargs)


class FeedbackReportPage(CreateView):
   template_name = 'library/contact.html'
   form_class = FeedbackReportForm

   def post(self, request, *args, **kwargs):
      form = FeedbackReportForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request, "Thanks for your feedback/report. Thanks for supporting us!!!")
         return redirect("Library:feedback_report")
         
      return render(request, self.template_name, {
         'form': form
      })


def add_to_cart(request, book_id):
   cart_arr = [int(book_id)]

   if 'cart' in request.COOKIES:
      print(request.COOKIES)
      if request.COOKIES['cart'] == '':
         cart_arr = []
      else:
         cart_arr = json.loads(request.COOKIES['cart'])
      if book_id not in request.COOKIES['cart']:         
         cart_arr.append(int(book_id))

   cart_json = json.dumps(cart_arr)

   response = HttpResponse('Cart Updated')
   response.set_cookie(key='cart', value=cart_json, expires=60*60*24*365)
   return response



class CategoryBasedPage(TemplateView):
   template_name = 'library/category_based.html'

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      category = Category.objects.get(pk=kwargs['category_id'])
      page_context['books'] = Book.objects.filter(category=category).order_by('-id')
      page_context['category_name'] = category.name
      return page_context

   




