# Generated by Django 2.2 on 2020-02-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20200227_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='permalink',
        ),
        migrations.RemoveField(
            model_name='work',
            name='permalink',
        ),
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(default='http://example.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='new_tab',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='work',
            name='link',
            field=models.URLField(default='http://example.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='new_tab',
            field=models.BooleanField(default=False),
        ),
    ]
