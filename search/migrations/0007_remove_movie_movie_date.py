# Generated by Django 2.2 on 2019-04-22 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20190422_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_date',
        ),
    ]
