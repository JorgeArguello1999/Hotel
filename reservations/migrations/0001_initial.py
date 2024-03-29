# Generated by Django 5.0.2 on 2024-02-19 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reservation_status', models.BooleanField(default=True)),
                ('entry_date', models.DateField()),
                ('out_date', models.DateField()),
                ('adults', models.IntegerField()),
                ('childrens', models.IntegerField(blank=True, null=True)),
                ('third_age', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clientsmodel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.roomsmodel')),
            ],
        ),
    ]
