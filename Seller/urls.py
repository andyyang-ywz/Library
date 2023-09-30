from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AddProductPage

app_name = "Seller"
urlpatterns = [
   path('add_product/', login_required(AddProductPage.as_view()), name='add_product')
]