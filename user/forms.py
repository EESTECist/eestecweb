from django import forms
from .models import ExtendedUser, Team


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ExtendedUser
        fields = ('username', 'first_name', 'last_name', 'password', 'image', 'bio')


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ExtendedUser
        fields = ('username', 'password')


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ('slug', 'president', 'members', 'active')