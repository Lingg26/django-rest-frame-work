# Generated by Django 4.1.1 on 2022-12-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CheckOut', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]