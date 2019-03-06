import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Writer(models.Model):
    class Meta:
        verbose_name = 'Writer'
        verbose_name_plural = 'Writers'
        app_label = 'pdblog'

    name = models.CharField(max_length=15)
    registered_date = models.DateTimeField('date registered')
    email_address = models.EmailField(max_length=254)


class Article(models.Model):
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-pub_date']
        app_label = 'pdblog'

    title = models.CharField(max_length=20)
    text = models.TextField(default="")
    pub_date = models.DateTimeField('date published', auto_now=True)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
