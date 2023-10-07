from django import forms
from Library.models import Book
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

class NewSellerForm(forms.ModelForm):
   class Meta:
      model = Seller
      fields = ['store_name', 'image', 'desc', 'location']
      widgets = {
         'store_name': forms.TextInput(attrs={
            'class': 'w-full bg-transparent border-b border-slate-200 my-5 text-2xl placeholder:text-neutral-300 outline-none',
            'placeholder': 'Input Your Name'
         }),
         'desc': forms.Textarea(attrs={'class': 'w-full bg-neutral-600 mt-2 p-3 resize-none outline-none'}),
         'image': forms.FileInput(attrs={'class': 'hidden'}),
         'location': forms.TextInput(attrs={
            'class': 'w-3/5 rounded-sm px-2 py-[6px] text-sm text-black outline-none',
            'placeholder': 'your location'
         })
      }
