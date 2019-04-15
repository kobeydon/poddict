from django import forms
from pdblog.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [ 'title', 'text']

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
