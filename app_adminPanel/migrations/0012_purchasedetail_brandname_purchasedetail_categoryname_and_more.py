# Generated by Django 4.2.6 on 2023-10-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0011_purchasemaster_brandname_purchasemaster_categoryname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedetail',
            name='BrandName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedetail',
            name='CategoryName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedetail',
            name='ColorName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedetail',
            name='SizeName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
