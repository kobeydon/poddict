from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import(
    AuthenticationForm, UserCreationForm
)
from django.contrib.auth import get_user_model
from django.db import models

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
            labels = { 'user_icon_thumbnail': _('User Icon (optional)')}
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
            fields = ( 'email', 'user_name', 'user_icon_thumbnail', 'first_name', 'last_name')
            labels = { 'user_icon_thumbnail':_('User Icon (optional)'),
                     'first_name':_('First Name (optional)'),
                     'last_name':_('Last Name( optional)')
                     }
            # blank = { 'user_icon_thumbnail':True }
        else:
            fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
