# Generated by Django 5.0.2 on 2024-02-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_roomsmodel_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomsmodel',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
