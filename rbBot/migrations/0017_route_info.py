# Generated by Django 3.2 on 2021-07-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbBot', '0016_auto_20210715_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='info',
            field=models.TextField(default='{"routes" : []}'),
        ),
    ]
