# Generated by Django 5.0.6 on 2024-06-27 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='flash_sales',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='product',
            name='top_deal',
            field=models.BooleanField(default=False),
        ),
    ]
