# Generated by Django 2.1.2 on 2019-05-25 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(default='')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('is_published', models.BooleanField(default=False)),
                ('slug', models.SlugField(default='')),
                ('likes', models.ManyToManyField(blank=True, related_name='article_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length='128')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('is_published', models.BooleanField(default=False)),
                ('target_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdblog.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='AllArticles',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('pdblog.article',),
        ),
        migrations.CreateModel(
            name='AllComments',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('pdblog.comment',),
        ),
    ]
