from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone
from navigation.models import Category
from Seller.models import Seller

# Create your models here.
def minimum_price(value):
   if value > 0:
      return value
   else:
      return ValidationError('Please input price of more than $0')


class Book(models.Model):
   name           = models.CharField(max_length=255, unique=True)
   author         = models.CharField(max_length=150)
   category       = models.ForeignKey(Category, on_delete=models.CASCADE)
   desc           = models.TextField(blank=True)
   synopsis       = models.TextField(blank=True)
   publisher      = models.CharField(max_length=150)
   total_pages    = models.PositiveIntegerField()
   total_chapters = models.PositiveIntegerField()
   publish_year   = models.PositiveIntegerField()
   stock          = models.PositiveIntegerField()
   weight         = models.PositiveIntegerField()
   size           = models.CharField(max_length=100)
   serial_number  = models.CharField(max_length=13)
   price          = models.DecimalField(decimal_places=2, max_digits=10,validators=[minimum_price])
   created_at     = models.DateTimeField(auto_now_add=True)
   seller         = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True)

   def __str__(self):
      return f"{self.name} | ${self.price}"


class BookPicture(models.Model):
   image         = models.ImageField(upload_to='book_picture/')
   book          = models.ForeignKey(Book, on_delete=models.CASCADE)
   is_main_image = models.BooleanField(default=False)

   def __str__(self):
      return f"Image for {self.book.name}"


class Transaction(models.Model):
   address         = models.CharField(max_length=150)
   payment_method  = models.CharField(max_length=100)
   shipment_method = models.CharField(max_length=100)
   book            = models.ForeignKey(Book, on_delete=models.CASCADE)
   user            = models.ForeignKey(User, on_delete=models.CASCADE)
   seller          = models.ForeignKey(Seller, on_delete=models.CASCADE)
   created_at      = models.DateTimeField(auto_now_add=True)
   arrival_status  = models.CharField(max_length=50, default="Waiting For Confirmations")
   arrive_date     = models.DateField(blank=True, null=True)
   # Waiting For Confirmations
   # Currently On Shipping
   # Book Arrived!

   
   def __str__(self):
      return f"{self.book.name} | {self.user.username} - {self.address}"

   def save(self, *args, **kwargs):
      if self.arrival_status == 'Book Arrived!':
         self.arrive_date = timezone.now()
      super(Transaction, self).save(*args, **kwargs)


class FeedbackReport(models.Model):
   name    = models.CharField(max_length=150)
   email   = models.EmailField()
   message = models.TextField()

   def __str__(self):
      return "Message from " + self.name

