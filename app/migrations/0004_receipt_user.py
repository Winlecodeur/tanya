# Generated by Django 5.1.6 on 2025-02-11 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.membre'),
        ),
    ]
