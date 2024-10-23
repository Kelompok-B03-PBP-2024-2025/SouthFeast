# Generated by Django 5.1.2 on 2024-10-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('kecamatan', models.CharField(choices=[('Kebayoran Lama', 'Kebayoran Lama'), ('Kebayoran Baru', 'Kebayoran Baru'), ('Cilandak', 'Cilandak'), ('Jagakarsa', 'Mampang Prapatan'), ('Pancoran', 'Pancoran'), ('Pasar Minggu', 'Pasar Minggu'), ('Pesanggrahan', 'Pesanggrahan'), ('Setiabudi', 'Setiabudi'), ('Tebet', 'Tebet')], max_length=100)),
                ('location', models.TextField(help_text='Detailed address of the restaurant')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]