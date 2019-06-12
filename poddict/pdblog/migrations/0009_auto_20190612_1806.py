# Generated by Django 2.1.8 on 2019-06-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdblog', '0008_article_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allarticles',
            options={'verbose_name': 'Article'},
        ),
        migrations.AlterModelOptions(
            name='allcomments',
            options={'verbose_name': 'Comment'},
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(choices=[('TC', 'Tech'), ('PD', 'Poddcast'), ('NT', 'Notes')], default='TC', max_length=2),
        ),
    ]
