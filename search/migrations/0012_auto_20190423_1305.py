# Generated by Django 2.2 on 2019-04-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_auto_20190423_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
    ]
