# Generated by Django 2.1.8 on 2019-06-10 02:45

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('pdblog', '0005_auto_20190610_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=markdownx.models.MarkdownxField(max_length=3000),
        ),
    ]