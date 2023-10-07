from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserDetail

@receiver(post_save, sender=User)
def create_userdetail(sender, instance, created, **kwargs):
   if created:
      UserDetail.objects.create(user=instance)