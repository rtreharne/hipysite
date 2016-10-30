from django import forms
from hello.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('first_name', 'last_name', 'email')

    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}
        )
    )

    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last Name'}
        )
    )

    email = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        )
    )

    depatment = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'UoL Department / Organisation Name'}
        )
    )
