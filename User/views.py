from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate
from django.db.models import Q
from Library.models import Book, Transaction
from Seller.models import Seller
from .models import UserDetail
from .forms import UserRegistrationForm, LoginForm, EditUserForm, EditUserDetailForm, ChangePasswordForm, SetAddressForm
import os

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
      return reverse_lazy('User:sign_in')
   
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
      return reverse_lazy('Library:main')

class LogoutPage(LogoutView):
   next_page = 'User:sign_in'

class ProfilePage(TemplateView):
   template_name = 'user/profile.html'

   def get_context_data(self, **kwargs):
      page_context = super().get_context_data()
      page_context['books'] = Book.objects.order_by('-id').all()[:10]
      page_context['on_going_transactions'] = Transaction.objects.filter(user=self.request.user).filter\
                              (Q(arrival_status="Waiting For Confirmations") | Q(arrival_status="Currently On Shipping"))
      return page_context



class AboutAccountPage(FormView):
   template_name = 'user/about_account.html'


   def get(self, request, *args, **kwargs):
      return render(request, self.template_name, {
         'form': EditUserForm(instance=self.request.user),
         'form2': EditUserDetailForm(instance=self.request.user.userdetail)
      })


   def post(self, request, *args, **kwargs):
      old_picture = request.user.userdetail.image
      
      form = EditUserForm({
         'username': request.POST['username'],
         'first_name': request.POST['first_name'],
         'last_name': request.POST['last_name'],
         'email': request.POST['email']
      }, instance=self.request.user)

      form2 = EditUserDetailForm({
         'gender': request.POST['gender'],
         'birthday': request.POST['birthday']
      }, request.FILES, instance=request.user.userdetail)

      if form.is_valid() and form2.is_valid():
         if 'image' in request.FILES:
            if old_picture != 'profile_picture/default.jpg':
               os.remove(old_picture.path)
         
         form.save()
         form2.save()

         messages.success(request, 'Your Account Is Successfully Updated')
         return redirect('User:about_account')

      return render(request, self.template_name, {
         'form': form,
         'form2': form2
      })


class PrivacySecurityPage(FormView):
   template_name = 'user/privacy_security.html'

   def get(self, request, *args, **kwargs):
      return render(request, self.template_name, {
         'form': ChangePasswordForm()
      })
   
   def post(self, request, *args, **kwargs):
      form = ChangePasswordForm(request.POST)
      if form.is_valid():
         if form.cleaned_data.get('new_password') != form.cleaned_data.get('confirm_password'):
            messages.error(request, 'Confirmation Password not valid! Please enter your new password again.')
            return redirect('User:privacy_security')
         if authenticate(request, username=request.user.username, password=form.cleaned_data.get('current_password')) is None:
            messages.error(request, 'You current password is incorrect! Please try again!')
            return redirect('User:privacy_security')
         
         request.user.set_password(form.cleaned_data.get('new_password'))
         request.user.save()
         messages.success(request, 'You password has been successfully updated!')
         return redirect('User:profile')

      return render(request, self.template_name, {
         'form': form
      })


class SetAddressPage(FormView):
   template_name = 'user/set_address.html'
   form_class = SetAddressForm

   def get(self, request, *args, **kwargs):
      form = SetAddressForm()
      if 'saved_address' in request.COOKIES:
         form = SetAddressForm(initial={'address': request.COOKIES['saved_address']})

      return render(request, self.template_name, {'form': form})
         
         

   def post(self, request, *args, **kwargs):
      messages.success(request, 'Location has been saved!')
      response = redirect('User:profile')
      response.set_cookie(key='saved_address', value=request.POST['address'], expires=60*60*24*365)
      return response



class TransactionHistory(TemplateView):
   template_name = 'user/transaction_history.html'



class UserCartList(TemplateView):
   template_name = 'user/cart_list.html'





