from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'input',
        'class': 'Input-text',
        'placeholder': 'Логин',
    }))
    password = forms.CharField(widget=forms.PasswordInput({
        'id': 'input',
        'class': 'Input-text',
        'placeholder': 'Пароль',
    }))


class UserRegistrationForm(forms.ModelForm):
    """ Формы для регистрации """
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'id': 'input',
            'class': 'Input-text',
            'placeholder': 'Пароль',
        }))
    password2 = forms.CharField(
        label='Подверждение пароля',
        widget=forms.PasswordInput(attrs={
            'id': 'input',
            'class': 'Input-text',
            'placeholder': 'Подверждение пароля',
        }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'id': 'input',
                'class': 'Input-text',
                'placeholder': 'Логин',
            }),
            'first_name': forms.TextInput(attrs={
                'id': 'input',
                'class': 'Input-text',
                'placeholder': 'Имя',
            }),
            'last_name': forms.TextInput(attrs={
                'id': 'input',
                'class': 'Input-text',
                'placeholder': 'Фамилия',
            }),
            'email': forms.EmailInput(attrs={
                'id': 'input',
                'class': 'Input-text',
                'placeholder': 'E-mail',
            })
        }

    def clean_password2(self):
        """Проверка на совпадение двух паролей"""
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']