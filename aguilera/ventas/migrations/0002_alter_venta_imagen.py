# Generated by Django 4.1.5 on 2023-01-13 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='imagen',
            field=models.CharField(max_length=200),
        ),
    ]
