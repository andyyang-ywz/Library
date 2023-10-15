from django import forms
from Library.models import Book, BookPicture
from Seller.models import Seller

class NewProductForm(forms.ModelForm):
   class Meta:
      model = Book
      exclude = ['created_at']
      widgets = {
         'name': forms.TextInput(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
         'author': forms.TextInput(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
         'category': forms.HiddenInput(),
         'desc': forms.Textarea(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none resize-none'}),
         'synopsis': forms.Textarea(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none resize-none'}),
         'publisher': forms.TextInput(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
         'publish_year': forms.NumberInput(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
         'stock': forms.NumberInput(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
         'total_pages': forms.NumberInput(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
         'total_chapters': forms.NumberInput(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
         'weight': forms.NumberInput(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
         'size': forms.HiddenInput(),
         'serial_number': forms.TextInput(attrs={'class': 'block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
         'price': forms.TextInput(attrs={'class': 'coma-regexed block w-full border border-slate-500 px-3 py-2 text-sm outline-none'}),
      }

class SellerDataForm(forms.ModelForm):
   class Meta:
      model = Seller
      fields = ['store_name', 'phone_number','image', 'desc', 'location']
      widgets = {
         'store_name': forms.TextInput(attrs={
            'class': 'w-full bg-transparent border-b border-slate-500 pb-1 placeholder:text-neutral-400 outline-none',
            'placeholder': 'Input Your Store Name',
            'autocomplete': 'off'
         }),
         'phone_number': forms.TextInput(attrs={
            'class': 'block w-full border border-neutral-500 outline-none p-2 text-sm',
            'placeholder': 'enter a valid phone number'
         }),
         'desc': forms.Textarea(attrs={'class': 'w-full border border-neutral-500 rounded-sm p-3 outline-none resize-none'}),
         'image': forms.FileInput(attrs={'class': 'hidden'}),
         'location': forms.TextInput(attrs={
            'class': 'block w-full border border-neutral-500 outline-none p-2 text-sm',
            'placeholder': 'your location'
         })
      }
