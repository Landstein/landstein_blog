# Generated by Django 2.2 on 2020-03-07 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20200227_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]