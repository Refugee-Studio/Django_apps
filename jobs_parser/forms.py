from django import forms
from jobs_parser.models import Post

class user_input(forms.ModelForm):
    position = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter position"
        })
    )
    location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter location"
        })
    )
