# Generated by Django 4.2.6 on 2023-12-15 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0055_remove_invoice_supplier_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchaseMaster',
        ),
    ]
