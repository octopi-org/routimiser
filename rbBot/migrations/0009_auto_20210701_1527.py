# Generated by Django 3.2 on 2021-07-01 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbBot', '0008_auto_20210701_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='current_route',
            new_name='latest_message',
        ),
        migrations.AddField(
            model_name='route',
            name='current_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbBot.planningsession'),
        ),
    ]
