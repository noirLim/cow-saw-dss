# Generated by Django 4.2.8 on 2023-12-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sapi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_sapi', models.CharField(max_length=6, unique=True)),
                ('nama_sapi', models.TextField()),
                ('desc_sapi', models.TextField()),
            ],
        ),
    ]
