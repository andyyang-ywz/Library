from django.contrib import admin
from .models import Book, BookPicture, Transaction, FeedbackReport

# Register your models here.
admin.site.register(Book)
admin.site.register(BookPicture)
admin.site.register(Transaction)
admin.site.register(FeedbackReport)
