from django import forms
from .models import Book
class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_price(self):
        if self.cleaned_data['price'] <=0:
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']

