# Generated by Django 4.1.4 on 2022-12-21 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='timestamp',
            field=models.DateField(verbose_name='date issued'),
        ),
    ]
