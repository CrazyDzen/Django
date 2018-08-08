from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', required=True,
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, max_length=32,
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        self.user = self.login()
        if not self.login():
            raise forms.ValidationError('Неверный логин или пароль')
        return super(LoginForm, self).clean(*args, **kwargs)

    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return authenticate(username=username, password=password)


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(label='Confirm password', required=True, max_length=32,
                                       widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email-address', required=True, max_length=32,
                            widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'username': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'password': forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.widgets.TextInput(attrs={'class': 'form-control'})
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(password)
        if commit:
            user.save()
        return user
