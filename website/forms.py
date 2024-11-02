from django import forms
from django.contrib.auth.models import User

from website.models import Product


class ObjctForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username",widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(min_length=3, label="Pssword", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']