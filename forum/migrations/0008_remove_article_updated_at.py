# Generated by Django 5.1.2 on 2024-10-23 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_article_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
    ]