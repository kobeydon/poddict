import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    class Meta:
        verbose_name = '質問'
        verbose_name_plural = '質問'
        ordering = ['question_text', '-pub_date']
        app_label = 'polls'

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def registered_choices(self):
        return self.choice_set.count()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
