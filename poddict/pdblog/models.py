import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-pub_date']
        app_label = 'pdblog'

    pdblog_title = models.CharField(max_length=20)
    pdblog_text = models.CharField(max_length=700)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.pdblog_title


class Writer(models.Model):
    class Meta:
        verbose_name = 'Writer'
        verbose_name_plural = 'Writers'
        app_label = 'pdblog'

    pdwriter_name = models.CharField(max_length=15)
    registered_date = models.DateTimeField('date registered')
    email_address = models.EmailField(max_length=254)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
