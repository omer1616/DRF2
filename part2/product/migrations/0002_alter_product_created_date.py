# Generated by Django 4.1.7 on 2023-03-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
