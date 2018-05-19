from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class FormUserCreation(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(FormUserCreation, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control form-control-lg',
                                                     'placeholder': "Имя пользователя"}
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs = {'class': 'form-control form-control-lg',
                                                'placeholder': "Пароль"}
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs = {'class': 'form-control form-control-lg',
                                                 'placeholder': "Подтверждение пароля"}
        self.fields['password2'].label = ''

class FormAuthentication(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormAuthentication, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control form-control-lg',
                                                     'placeholder': "Имя пользователя"}
        self.fields['username'].label = ''

        self.fields['password'].widget.attrs = {'class': 'form-control form-control-lg',
                                                 'placeholder': "Пароль"}
        self.fields['password'].label = ''



