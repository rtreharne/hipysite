from django import forms
from hello.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('first_name', 'last_name', 'email', 'department', 'profile', 'song')

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

    department = forms.ChoiceField(
        choices=[
            ('', "Department"),
            ('', "----------"),
            ("Biology", "Biology"),
            ("Biostatistics", "Biostatistics"),
            ("Chemistry", "Chemistry"),
            ("Computer Science", "Computer Science"),
            ("Earth, Ocean, Ecology", "Earth, Ocean & Ecological Sciences"),
            ("EEE", "Electrical Engineering and Electronics"),
            ("Engineering", "Engineering"),
            ("Geology", "Geology"),
            ("Mathematics", "Mathematical Sciences"),
            ("Physics", "Physics"),
            ("Astrophysics", "Astrophysics"),
            ("External", "External Group/Business/Organisation"),
            ("Other", "Other")
        ],
        label="",
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Department'}
        )
    )

    profile = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Link to online profile (e.g. https://linkedin.com/in/<MY_PROFILE>)'}
        )
    )

    song = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Song for Hive playlist (e.g. The Beatles, "Yellow Submarine")'}
        )
    )
