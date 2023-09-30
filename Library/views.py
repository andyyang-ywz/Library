from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Book


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
      page_context['book_img'] = (book.id - 14) * -1
      page_context['books'] = self.get_recommended_book(book)

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
