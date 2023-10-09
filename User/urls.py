from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import WelcomePage, SignUpPage, SignInPage, LogoutPage, ProfilePage, AboutAccountPage, PrivacySecurityPage

app_name = "User"
urlpatterns = [
   path('', WelcomePage.as_view(), name='welcome'),
   path('sign-up', SignUpPage.as_view(), name='sign_up'),
   path('sign-in', SignInPage.as_view(), name='sign_in'),
   path('user/logout', login_required(LogoutPage.as_view()), name='logout'),
   path('user/profile', login_required(ProfilePage.as_view()), name='profile'),
   path('user/profile/about-account', login_required(AboutAccountPage.as_view()), name='about_account'),
   path('user/profile/privacy-security', login_required(PrivacySecurityPage.as_view()), name='privacy_security'),
]