from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username = email , password=password)
        print(email, password)
        if not user or not user.is_active:
            raise forms.ValidationError("Неверный логин или пароль.")
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username = email , password=password)
        return user
