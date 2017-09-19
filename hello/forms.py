from django import forms
from hello.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('first_name', 'last_name', 'email', 'department', 'profile', 'song', 'hear')

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
            ("Alt-C", "Alt-C Conference Delegate"),
            ("Architecture", "Architecture"),
            ("Astrophysics", "Astrophysics"),
            ("Biology", "Biology"),
            ("Biostatistics", "Biostatistics"),
            ("Chemistry", "Chemistry"),
            ("Computer Science", "Computer Science"),
            ("Cummunications and Media", "Communications and Media"),
            ("Earth, Ocean, Ecology", "Earth, Ocean & Ecological Sciences"),
            ("EEE", "Electrical Engineering and Electronics"),
            ("Engineering", "Engineering"),
            ("English", "English"),
            ("Geography and Planning", "Geography and Planning"),
            ("Geology", "Geology"),
            ("Institute of Infection /  Global Health", "Institute of Infection / Global Health"),
            ("Law", "Law"),
            ("Management School", "Management School"),
            ("Mathematics", "Mathematical Sciences"),
            ("Music", "Music"),
            ("Philosophy", "Philosophy"),
            ("Physics", "Physics"),
            ("Politics", "Politics"),
            ("Sociology", "Sociology"),
            ("Stephenson Institute", "Stephenson Institute"),
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

    hear = forms.ChoiceField(
        choices=[
            ("", "How did you hear about HiPy?"),
            ('', "----------"),
            ("Poster/Flyer", "Poster/Flyer"),
            ("Word of mouth", "Word of mouth"),
            ("Email", "Email"),
            ("UoL video screen", "UoL video screen"),
            ("The Google Overlords", "The Google Overlods"),
            ("Other", "Other")
        ],
        required=True,
        label="",
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'How did you hear about HiPy/LivIDEA?'}
        )
    )
