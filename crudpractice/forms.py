from django import forms

from .models import Book
class Bookform(forms.ModelForm):

   class Meta:
     mode=Book
     fields=('title','author','publication_date','genre')

