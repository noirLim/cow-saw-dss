# Generated by Django 4.2.8 on 2024-01-31 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nilai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='max',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='min',
            field=models.FloatField(),
        ),
    ]