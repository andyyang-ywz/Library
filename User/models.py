from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class UserDetail(models.Model):
   user     = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
   gender   = models.CharField(max_length=10, null=True, blank=True, choices=[
      ('Male', 'Male'),
      ('Female', 'Female'),
   ])
   image    = models.ImageField(upload_to='profile_picture/', default="profile_picture/default.jpg")
   birthday = models.DateField(null=True, blank=True)

   def __str__(self):
      return f"{self.user.username} Detailed Account"

   def save(self, *args, **kwargs):
      super(UserDetail, self).save(*args, **kwargs)
      if self.image:
         image = Image.open(self.image.path)
         image.thumbnail((230, 230))
         image.save(self.image.path)



   

