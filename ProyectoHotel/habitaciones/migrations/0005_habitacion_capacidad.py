# Generated by Django 5.0.3 on 2024-09-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0004_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='capacidad',
            field=models.IntegerField(default=1),
        ),
    ]
