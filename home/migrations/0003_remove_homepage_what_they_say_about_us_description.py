# Generated by Django 2.0.1 on 2019-06-11 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190611_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='what_they_say_about_us_description',
        ),
    ]