# Generated by Django 4.1.4 on 2023-02-15 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0003_alter_ingredient_qty_alter_ingredient_unit_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reciperequirement',
            old_name='menu_ingredient',
            new_name='ingredient',
        ),
        migrations.RemoveField(
            model_name='reciperequirement',
            name='recipe_qty',
        ),
        migrations.AddField(
            model_name='reciperequirement',
            name='qty',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]