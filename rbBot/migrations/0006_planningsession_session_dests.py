# Generated by Django 3.2 on 2021-06-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbBot', '0005_alter_route_destinations'),
    ]

    operations = [
        migrations.AddField(
            model_name='planningsession',
            name='session_dests',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
