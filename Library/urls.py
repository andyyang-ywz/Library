from django.urls import path
from django.contrib.auth.decorators import login_required
from.views import MainIndex, BookDetailPage, PurchasePage, PaymentProcessPage, FeedbackReportPage, add_to_cart, CategoryBasedPage


app_name = 'Library'
urlpatterns = [
   path('', MainIndex.as_view(), name="main"),
   path('book/<pk>', BookDetailPage.as_view(), name="book_detail"),
   path('purchase_book/<book_id>', login_required(PurchasePage.as_view()), name='purchase'),
   path('purchase_book/payment_process/<address>/<shipment_method>/<payment_method>/<book_id>', login_required(PaymentProcessPage.as_view()), name='payment_process'),
   path('feedback-report/contact-us', FeedbackReportPage.as_view(), name='feedback_report'),
   path('book/add-to-cart/<book_id>', add_to_cart, name="add_to_cart"),
   path('category/<category_id>', CategoryBasedPage.as_view(), name="category_based")
]