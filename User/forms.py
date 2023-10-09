from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.contrib.auth import password_validation
from .models import UserDetail

class UserRegistrationForm(UserCreationForm):
   email = forms.EmailField(widget=forms.EmailInput(attrs=
            {'class': 'w-full border border-neutral-500 text-[13px] md:text-sm p-[6px] outline-none'}
         ))
   first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs=
            {'class': 'w-full border border-neutral-500 text-[13px] md:text-sm p-[6px] outline-none'}
         ))
   last_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs=
            {'class': 'w-full border border-neutral-500 text-[13px] md:text-sm p-[6px] outline-none'}
         ))
   password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=
            {'class': 'w-full border border-neutral-500 text-[13px] md:text-sm p-[6px] outline-none'}
         ))
   password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=
            {'class': 'w-full border border-neutral-500 text-[13px] md:text-sm p-[6px] outline-none'}
         ))

   class Meta:
      model = User
      fields = ['username', 'email', 'first_name', 'last_name']
      widgets = { 
         'username': forms.TextInput(attrs=
            {'class': 'w-full border border-neutral-500 text-[13px] md:text-sm p-[6px] outline-none'}
         ),
      }

   def clean_email(self):
      data = self.cleaned_data["email"]
      data_arr = data.split('@')
      valid_email_ext = ['gmail.com', 'email.com', 'yahoo.co.id']
      if data_arr[-1] not in valid_email_ext:
         raise ValidationError('Please use a valid email address!')
      
      return data


class LoginForm(AuthenticationForm):
   username = forms.CharField(max_length=150, widget=forms.TextInput(attrs=
            {'class': 'w-full border border-neutral-500 text-[13px] md:text-sm p-[6px] outline-none'}
         ))
   password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs=
            {'class': 'w-full border border-neutral-500 text-[13px] md:text-sm p-[6px] outline-none'}
         ))

class EditUserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email']
      widgets = {
         'username': forms.TextInput(attrs={
            'class': 'block w-full border border-slate-500 rounded-sm mt-1 p-2 text-sm outline-none'
         }),
         'first_name': forms.TextInput(attrs={
            'class': 'block w-full border border-slate-500 rounded-sm mt-1 p-2 text-sm outline-none'
         }),
         'last_name': forms.TextInput(attrs={
            'class': 'block w-full border border-slate-500 rounded-sm mt-1 p-2 text-sm outline-none'
         }),
         'email': forms.EmailInput(attrs={
            'class': 'block w-full border border-slate-500 rounded-sm mt-1 p-2 text-sm outline-none'
         }),
      }

class EditUserDetailForm(forms.ModelForm):
   class Meta:
      model = UserDetail
      exclude = ['user']
      widgets = {
         'gender': forms.HiddenInput(attrs={
            'class': 'block w-full border border-slate-500 rounded-sm mt-1 p-2 text-sm outline-none'
         }),
         'image': forms.FileInput(attrs={
            'class': 'hidden'
         }),
         'birthday': forms.DateInput(attrs={
            'class': 'hidden'
         })
      }


class ChangePasswordForm(forms.Form):
   current_password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=
            {'class': 'w-full border border-neutral-500 p-2 mt-1 text-sm outline-none'}
         ))
   new_password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=
            {'class': 'w-full border border-neutral-500 p-2 mt-1 text-sm outline-none'}
         ), validators=[MinLengthValidator(8)])
   confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs=
            {'class': 'w-full border border-neutral-500 p-2 mt-1 text-sm outline-none'}
         ))

   def clean_new_password(self):
      new_password = self.cleaned_data.get('new_password')
      try: 
         password_validation.validate_password(new_password, self)
      except forms.ValidationError as error:
         self.add_error('new_password', error)

      return new_password

      