# Generated by Django 5.1.2 on 2024-10-24 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_reviewentry_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewentry',
            name='image',
        ),
    ]