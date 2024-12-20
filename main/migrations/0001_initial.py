# Generated by Django 5.1.2 on 2024-10-20 13:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makanan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=100)),
                ('image', models.TextField()),
                ('description', models.TextField()),
                ('categories', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('resto_name', models.CharField(max_length=250)),
                ('kecamatan', models.CharField(max_length=200)),
                ('location', models.TextField()),
            ],
        ),
    ]
