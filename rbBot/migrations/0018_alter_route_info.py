# Generated by Django 3.2 on 2021-07-20 14:40

from django.db import migrations, models
import rbBot.models


class Migration(migrations.Migration):

    dependencies = [
        ('rbBot', '0017_route_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='info',
            field=models.JSONField(default=rbBot.models.routeInfo_default_value),
        ),
    ]
