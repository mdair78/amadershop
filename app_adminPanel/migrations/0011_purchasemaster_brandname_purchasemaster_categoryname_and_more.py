# Generated by Django 4.2.6 on 2023-10-21 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0010_productlist_categoryname_productlist_colorname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasemaster',
            name='BrandName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasemaster',
            name='CategoryName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasemaster',
            name='ColorName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasemaster',
            name='SizeName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
