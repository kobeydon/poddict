import datetime
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from register.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

class Article(models.Model):
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-pub_date']
        app_label = 'pdblog'

    title = models.CharField(max_length=128)
    text = models.TextField(default="")
    pub_date = models.DateTimeField('date published', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    favorites = models.ManyToManyField(User, related_name='favorites')
    slug = models.SlugField(default="")
    # comments = models.TextField(max_length=140)
    #uses custom manager for general view
    objects = ArticleManager()

    def __str__(self):
        return self.title

    @property
    def total_fav(self):
        return self.favorites.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)




class AllArticles(Article):
    class Meta:
        proxy = True

    objects = models.Manager()