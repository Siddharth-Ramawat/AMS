from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.validators import RegexValidator
from .models import Profile
import datetime


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 2)]


def current_year():
    return datetime.date.today().year


CSE = 'COMPUTER SCIENCE AND ENGINEERING'
IT = 'INFORMATION TECHNOLOGY'
ECE = 'ELECTRONICS AND COMMUNICATION ENGINEERING'
EEE = 'ELECTRICAL AND ELECTRONIC ENGINEERING'
ME = 'MECHANICAL ENGINEERING'
CE = 'CIVIL ENGINEERING'
NONE = ''

DEPT_CHOICES = (
    (NONE, ''),
    (CSE, 'COMPUTER SCIENCE AND ENGINEERING'),
    (IT, 'INFORMATION TECHNOLOGY'),
    (ECE, 'ELECTRONICS AND COMMUNICATION ENGINEERING'),
    (EEE, 'ELECTRICAL AND ELECTRONIC ENGINEERING'),
    (ME, 'MECHANICAL ENGINEERING'),
    (CE, 'CIVIL ENGINEERING'),
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileRegisterForm(forms.ModelForm):
    registration_number = forms.CharField(max_length=12, validators=[RegexValidator('^(\d{2}\w\d{2}\w\d{2}\w{2})$',
                                                                                    message="Registration number "
                                                                                            "should be in the form of "
                                                                                            "16K81A0501")])
    job_role = forms.CharField(max_length=100, required=False)
    work_location = forms.CharField(max_length=100, required=False)
    company = forms.CharField(max_length=200, required=False)
    passout_year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)

    class Meta:
        model = Profile
        fields = ['dept', 'registration_number', 'job_role', 'work_location', 'company']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        return self.cleaned_data['email'].lower()


class ProfileUpdateForm(forms.ModelForm):
    registration_number = forms.CharField(max_length=12, required=False)
    job_role = forms.CharField(max_length=100, required=False)
    work_location = forms.CharField(max_length=100, required=False)
    company = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Profile
        fields = ['dept', 'registration_number', 'job_role', 'work_location', 'company', 'image']

    def clean_registration_number(self):
        return self.cleaned_data['registration_number'].upper()
