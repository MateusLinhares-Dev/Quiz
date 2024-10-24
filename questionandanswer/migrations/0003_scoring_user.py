# Generated by Django 5.1.2 on 2024-10-21 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('questionandanswer', '0002_scoring'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoring',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='points_player', to='player.player'),
            preserve_default=False,
        ),
    ]