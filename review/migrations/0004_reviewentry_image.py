# Generated by Django 5.1.2 on 2024-10-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_rename_product_reviewentry_menu_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='review_images/'),
        ),
    ]