from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control js-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control js-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control js-input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control js-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control js-input'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control js-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control js-input'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            raise forms.ValidationError("Wrong username and password combination.")
        if not user.is_active:
            raise forms.ValidationError("Your account is not active.")

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
