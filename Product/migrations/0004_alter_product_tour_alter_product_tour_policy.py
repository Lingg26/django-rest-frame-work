# Generated by Django 4.1.1 on 2022-12-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_remove_product_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tour',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='tour_policy',
            field=models.CharField(max_length=1000),
        ),
    ]
