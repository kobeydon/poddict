from django import forms
from pdblog.models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [ 'title', 'text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'comment_text']

class ContactForm(forms.Form):

    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(required=False)
    cc_myself = forms.BooleanField(required=False)
