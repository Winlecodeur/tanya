# Generated by Django 5.1.6 on 2025-02-06 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('given_name', models.CharField(max_length=150)),
                ('number', models.PositiveBigIntegerField()),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('given_name', models.CharField(max_length=150)),
                ('birth', models.DateField()),
                ('address', models.CharField(max_length=300)),
                ('number', models.PositiveIntegerField()),
                ('bio', models.TextField()),
                ('date_acquired', models.DateTimeField(auto_now_add=True)),
                ('money_GIVE', models.PositiveBigIntegerField()),
                ('children', models.PositiveBigIntegerField()),
                ('infos_children', models.TextField()),
                ('spouse', models.CharField(max_length=150)),
                ('statut', models.CharField(choices=[('MARIE', 'marié'), ('CELIBATAIRE', 'celibataire'), ('VEUVE', 'veuve')], default='VEUVE', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('size', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Propriete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propriete', to='app.membre')),
                ('space', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='spaces', to='app.space')),
            ],
        ),
    ]
