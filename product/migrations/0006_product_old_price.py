# Generated by Django 5.0.6 on 2024-06-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_category_product_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
