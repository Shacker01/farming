# Generated by Django 4.1.2 on 2022-10-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_farmer_product_delete_farmers_delete_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Image',
            field=models.ImageField(upload_to='media/products'),
        ),
    ]
