# Generated by Django 4.2.6 on 2023-11-23 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0023_remove_orderdetail_brand_remove_orderdetail_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductList',
        ),
    ]
