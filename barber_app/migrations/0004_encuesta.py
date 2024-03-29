# Generated by Django 5.0.1 on 2024-01-27 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_app', '0003_cita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('cita', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='barber_app.cita')),
            ],
        ),
    ]
