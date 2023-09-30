from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
   user     = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
   gender   = models.CharField(max_length=10, null=True, blank=True, choices=[
      ('Male', 'Male'),
      ('Female', 'Female'),
   ])
   image    = models.ImageField(upload_to='profile_picture/', default="default.jpg")
   birthday = models.DateField(null=True, blank=True)

   def __str__(self):
      return f"{self.user.username} Detailed Account"

