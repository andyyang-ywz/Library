from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AddProductPage, OpenSellerAccount, ProductImageUpload, SellerAccountPage, EditSellerAccountPage, EditProductPage, CustomerOrderPage, update_track

app_name = "Seller"
urlpatterns = [
   path('add-product/', login_required(AddProductPage.as_view()), name='add_product'),
   path('edit-product/<pk>', login_required(EditProductPage.as_view()), name='edit_product'),
   path('profile/open-seller-account', login_required(OpenSellerAccount.as_view()), name='open_seller_account'),
   path('product-image-upload/<book_id>', login_required(ProductImageUpload.as_view()), name='upload_image'),
   path('account/<seller_id>', login_required(SellerAccountPage.as_view()), name='account'),
   path('account/edit/<pk>', login_required(EditSellerAccountPage.as_view()), name='edit_seller_account'),
   path('customer_orders/', login_required(CustomerOrderPage.as_view()), name="customer_orders"),
   path('order/udpate_track/<order_id>', login_required(update_track), name="udpate_track"),
]