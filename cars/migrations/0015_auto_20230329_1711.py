# Generated by Django 3.2.18 on 2023-03-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_auto_20230329_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(default=19),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(default=18735),
        ),
    ]
