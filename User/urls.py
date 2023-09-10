from django.urls import path
from .views import WelcomePage

app_name = "User"
urlpatterns = [
   path('', WelcomePage.as_view(), name='welcome')
]