from django.forms import ModelForm, Form
from pdblog.models import Writer, Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

class WriterForm(ModelForm):
    class Meta:
        model = Writer
        fields = "__all__"
