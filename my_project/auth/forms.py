from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from catalog.models import Customer

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2', 'city', 'contact_phone', 'gender', 'age', 'address']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password']
