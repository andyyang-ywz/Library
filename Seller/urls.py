from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AddProductPage, OpenSellerAccount, ProductImageUpload

app_name = "Seller"
urlpatterns = [
   path('add-product/', login_required(AddProductPage.as_view()), name='add_product'),
   path('profile/open-seller-account', login_required(OpenSellerAccount.as_view()), name='open_seller_account'),
   path('product-image-upload/', login_required(ProductImageUpload.as_view()), name='upload_image'),
]