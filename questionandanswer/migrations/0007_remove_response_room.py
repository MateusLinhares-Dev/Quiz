# Generated by Django 5.1.2 on 2024-10-23 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0006_response_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='room',
        ),
    ]
