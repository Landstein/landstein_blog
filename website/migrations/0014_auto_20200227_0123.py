# Generated by Django 2.2 on 2020-02-27 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_social_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='work',
            name='body',
        ),
    ]