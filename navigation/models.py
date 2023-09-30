from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=50)
   is_fictional = models.BooleanField()
   last_updated = models.DateTimeField()
   
   def save(self, *args, **kwargs):
      self.last_updated = timezone.now()
      return super(Category, self).save(*args, **kwargs)

   def __str__(self):
      category_type = "Non-fictional"
      if self.is_fictional:
         category_type = "Fictional"

      return f"{category_type}: {self.name}"