from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from monolith.strings import HEIGHT, WEIGHT, HEIGHT_HELP, WEIGHT_HELP, OPTIONAL, REQUIRED
from monolith.models import Profile
from decimal import Decimal
from monolith.strings import STR_MALE, STR_FEMALE, STR_NOT_INFORMED, STR_AVERAGE_JOE, STR_ATHLETE


class BmiInputForm(forms.Form):
    height = forms.DecimalField(label=HEIGHT, min_value=Decimal('1'), max_value=Decimal('2.3'), help_text=HEIGHT_HELP)
    weight = forms.DecimalField(label=WEIGHT, min_value=Decimal('10'), max_value=Decimal('120'), help_text=WEIGHT_HELP)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text=OPTIONAL)
    last_name = forms.CharField(max_length=30, required=False, help_text=OPTIONAL)
    email = forms.EmailField(max_length=254, help_text=REQUIRED)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, help_text=REQUIRED)
    password = forms.CharField(max_length=30, help_text=REQUIRED, widget=forms.PasswordInput)


class TellMeMoreForm(forms.Form):
    MALE = 'MA'
    FEMALE = 'FE'
    NOT_INFORMED = 'NF'

    AVERAGE_JOE = 'AJ'
    ATHLETE = 'AT'

    YEARS = range(1960, 2020, 1)

    GENDER_CHOICES = [
        (MALE, STR_MALE),
        (FEMALE, STR_FEMALE),
        (NOT_INFORMED, STR_NOT_INFORMED),
    ]

    CONDITION_CHOICES = [
        (AVERAGE_JOE, STR_AVERAGE_JOE),
        (ATHLETE, STR_ATHLETE),
    ]
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
    )
    condition = forms.ChoiceField(
        choices=CONDITION_CHOICES,
    )


    class Meta:
        model = Profile
        fields = ('birthday', 'gender', 'condition')