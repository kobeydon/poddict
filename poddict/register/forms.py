from django import forms
from django.contrib.auth.forms import(
    AuthenticationForm, UserCreationForm
)
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):
    """login Form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.label == 'Password':
                field.widget.attrs['class'] = 'form-control input_pass'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs['class'] = 'form-control input_user'
                field.widget.attrs['placeholder'] = field.label

class UserCreateForm(UserCreationForm):
    """Form to Create User"""

    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('email', 'user_name', 'user_icon_thumbnail',)
        else:
            fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class UserUpdateForm(forms.ModelForm):
    """Form to update users"""

    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('email', 'user_name', 'user_icon_thumbnail', 'first_name', 'last_name')
        else:
            fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
