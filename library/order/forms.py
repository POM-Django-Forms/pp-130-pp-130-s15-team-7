from django import forms
from .models import Order
from book.models import Book
from django.utils.timezone import now

class OrderForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label="Book")
    plated_end_at = forms.DateTimeField(
        label="Return date",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=now
    )

    class Meta:
        model = Order
        fields = ['book', 'plated_end_at']