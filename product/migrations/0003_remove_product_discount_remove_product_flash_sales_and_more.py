# Generated by Django 5.0.6 on 2024-06-27 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='flash_sales',
        ),
        migrations.RemoveField(
            model_name='product',
            name='top_deal',
        ),
    ]