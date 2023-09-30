from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from Library.models import Book
from .models import UserDetail
from .forms import UserRegistrationForm, LoginForm, EditUserForm, EditUserDetailForm

# Create your views here.
class WelcomePage(TemplateView):
   template_name = 'index.html'

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      page_context['quotes'] = [
         {
            'author': 'Andy yang',
            "message": "Awareness is the key to self improvement. Control the ones you can control by being aware of what you are thinking and doing."
         },
         {
            'author': 'Ms.Capri',
            'message': "Be present at everything you do. Learn from the past, focus on the present, plan for the future.",
         },
         {
            'author': 'Davin Lim',
            'message': 'Be a true friend, not a friend that only come, asking for something.',
         },
         {
            'author': 'Serene Adrienelim',
            'message': "Do what ever you like to do as long as you don't bother others."
         },
         {
            'author': 'Veren Calista',
            'message': "Don't give up when you still have something to give, nothing is really over until the moment you stop trying."
         },
         {
            'author': 'David Goggins',
            'message': "Evaluate your life in its totality! We all waste so much time doing meaningless bullshits. Give it all for your 24 hours a day. Stay hard!!"
         },
         {
            'author': 'Ricky Howard',
            'message': "Don't ever complain on a situation, because the situation might be the key of your success."
         },
         {
            'author': 'Evandrew Khonan',
            'message': "How can you expect yourself to be a skilled sailor without any waves in the sea."
         },
         {
            'author': 'Friedrich Nietzche',
            'message': "To live is to suffer; to survive is to find some meaning in the suffering."
         },
         {
            'author': 'Jonathan Darren Choandry',
            'message': "When we see someones worth, we should think of equaling them. When we see a persons contrary character, we should turn inwards and examine ourselves"
         }
      ]
      return page_context

class SignUpPage(CreateView):
   form_class = UserRegistrationForm
   template_name = 'user/sign_up.html'

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      page_context['auth_page'] = True
      return page_context

   def get_success_url(self):
      messages.success(self.request, "You successfully created your account. You can now login!")
      return reverse_lazy('User:welcome')
   
   def get(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         return redirect('Library:main')
      
      return super(SignUpPage, self).get(request, *args, **kwargs)

class SignInPage(LoginView):
   form_class = LoginForm
   template_name = 'user/sign_in.html'

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      page_context['auth_page'] = True
      return page_context
   
   def get(self, request, *args, **kwargs):
      if request.user.is_authenticated:
         return redirect('Library:main')
      
      return super(SignInPage, self).get(request, *args, **kwargs)

   def get_success_url(self):
      messages.success(self.request, 'You have logged in to your account!')
      print('f asdfk asd;f jas;kldfj ;adklsjf;alksjfajsfjas;jflajkslfaskjfl ')
      return reverse_lazy('Library:main')

class LogoutPage(LogoutView):
   next_page = 'User:sign_in'

class ProfilePage(TemplateView):
   template_name = 'user/profile.html'

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      page_context['books'] = Book.objects.order_by('-id').all()[:10]
      return page_context



class AboutAccountPage(TemplateView):
   template_name = 'user/about_account.html'

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      page_context['form'] = EditUserForm(instance=self.request.user)
      user_detail = UserDetail.objects.get(pk=self.request.user)
      page_context['form2'] = EditUserDetailForm(instance=user_detail)
      return page_context


   


