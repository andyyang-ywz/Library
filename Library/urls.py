from django.urls import path
from django.contrib.auth.decorators import login_required
from.views import MainIndex, BookDetailPage


app_name = 'Library'
urlpatterns = [
   path('', MainIndex.as_view(), name="main"),
   path('book/<pk>', BookDetailPage.as_view(), name="book_detail"),
]