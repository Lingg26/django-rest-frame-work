# Generated by Django 4.1.1 on 2022-12-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CategoryList', '0002_alter_categorylist_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorylist',
            name='categoryItem',
        ),
        migrations.AlterField(
            model_name='categorylist',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='categorylist',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
