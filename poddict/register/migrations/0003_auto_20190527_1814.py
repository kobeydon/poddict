# Generated by Django 2.1.2 on 2019-05-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20190527_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_icon',
            field=models.ImageField(blank=True, default='user_icon/poddict_icon.png', height_field='icon_height', null=True, upload_to='user_icon/', width_field='icon_width'),
        ),
    ]