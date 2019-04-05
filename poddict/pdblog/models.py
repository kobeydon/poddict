import datetime
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from register.models import User
# Create your models here.

class Article(models.Model):
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-pub_date']
        app_label = 'pdblog'

    title = models.CharField(max_length=20)
    text = models.TextField(default="")
    pub_date = models.DateTimeField('date published', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    # favorite = models.IntegerField("Like!", default=0)

    def __str__(self):
        return self.title
