from django.contrib.auth.forms import(
    AuthenticationForm
)

class LoginForm(AuthenticationForm):
    """login Form"""

    def ___init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.value():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['paceholder'] = field.label
