# Generated by Django 3.2 on 2021-07-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbBot', '0009_auto_20210701_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='routes_created',
            field=models.IntegerField(default=0),
        ),
    ]
