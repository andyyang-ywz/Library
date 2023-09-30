from django import forms
from Library.models import Book

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