from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age', 'username', 'email', 'phone_number', 'password1', 'password2')
