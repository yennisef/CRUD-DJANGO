# Generated by Django 4.1.3 on 2022-11-23 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableMobil',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
