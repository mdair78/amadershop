# Generated by Django 4.2.6 on 2023-12-15 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0056_delete_purchasemaster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetail',
            old_name='UnitPreviousStock',
            new_name='PreviousStock',
        ),
        migrations.RenameField(
            model_name='productdetail',
            old_name='UnitStockInHand',
            new_name='StockInHand',
        ),
    ]
