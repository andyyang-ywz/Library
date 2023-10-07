from django.db import models
from PIL import Image
from User.models import User

# Create your models here.
class Seller(models.Model):
   user           = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='seller_account')
   store_name     = models.CharField(max_length=100)
   desc           = models.TextField()
   image          = models.ImageField(upload_to='store_picture/', null=False)
   location       = models.CharField(max_length=150)
   created_at     = models.DateTimeField(auto_now_add=True)
   account_active = models.BooleanField(default=False)

   def __str__(self):
      return f"{self.store_name} From Account - {self.user.username}"
   
   def save(self, *args, **kwargs):
      super(Seller, self).save(*args, **kwargs)
      if self.image:
         image = Image.open(self.image.path)
         image.thumbnail((230, 230))
         image.save(self.image.path)

