from django import forms
from pictures.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ("title", "image")
