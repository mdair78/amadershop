# Generated by Django 4.2.6 on 2023-10-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0006_returndetail_productcode_returndetail_productname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='ProductCode',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='ProductName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
