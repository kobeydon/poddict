from django import forms
from pdblog.models import Writer, Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

class WriterForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
