# Generated by Django 2.1.2 on 2019-05-27 07:46

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20190527_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_icon',
            field=models.ImageField(blank=True, default='/Users/Kohei/pythonprojects/myenv3/poddict/storage/user_icon/poddict_icon.png', height_field='icon_height', upload_to=register.models.user_directory_path, width_field='icon_width'),
        ),
    ]
