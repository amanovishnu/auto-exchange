# Generated by Django 3.2.18 on 2023-03-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_auto_20230312_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(default=8),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(default=98007),
        ),
    ]
