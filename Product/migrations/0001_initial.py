# Generated by Django 4.1.1 on 2022-12-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('category_id', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('vehicle', models.CharField(max_length=255)),
                ('starting_point', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('tour', models.CharField(max_length=255)),
                ('tour_policy', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('tour_code', models.CharField(max_length=255)),
                ('product_image', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(blank=True)),
                ('updatedAt', models.DateTimeField(blank=True)),
            ],
        ),
    ]
