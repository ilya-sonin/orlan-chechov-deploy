# Generated by Django 2.0.1 on 2019-07-17 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20190717_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onegallerypage',
            name='href',
        ),
    ]
