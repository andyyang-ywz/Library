from django import forms
from .models import Transaction, FeedbackReport

class TransactionForm(forms.ModelForm):
   class Meta:
      model = Transaction
      fields = ['address', 'shipment_method', 'payment_method']
      widgets = {
         'address': forms.TextInput(attrs={
            'class': 'w-full border border-neutral-600 p-2 mt-2 outline-none text-sm md:text-base',
            'placeholder': 'insert your address'
         }),
         'shipment_method': forms.HiddenInput(),
         'payment_method': forms.HiddenInput()
      }
      error_messages = {
         'address': { 'required': ['Please input your address'] },
         'payment_method': { 'required': ['Please input your payment method'] },
         'shipment_method': { 'required': ['Please input your shipping method'] }
      }

class FeedbackReportForm(forms.ModelForm):
   class Meta:
      model = FeedbackReport
      fields = "__all__"
      widgets = {
         'name': forms.TextInput(attrs={'class': 'w-full border border-neutral-500 rounded-sm my-1 p-2 text-sm outline-none'}),
         'email': forms.EmailInput(attrs={'class': 'w-full border border-neutral-500 rounded-sm my-1 p-2 text-sm outline-none'}),
         'message': forms.Textarea(attrs={'class': 'w-full border border-neutral-500 rounded-sm my-1 p-2 text-sm outline-none resize-none'})
      }