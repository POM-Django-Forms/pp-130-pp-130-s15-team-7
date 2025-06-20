from django import forms
from .models import Book
from author.models import Author

class BookForm(forms.ModelForm):
    authors_text = forms.CharField(
        required=False,
        label='Authors (separate names by comma)',
        widget=forms.TextInput(attrs={'placeholder': 'Author1, Author2, Author3'})
    )

    class Meta:
        model = Book
        fields = ['name', 'description', 'count']

        widgets = {
            'name': forms.TextInput(attrs={'maxlength': 128}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'count': forms.NumberInput(attrs={'min': 0}),
        }

    def clean_authors_text(self):
        data = self.cleaned_data.get('authors_text', '')
        return data.strip()