# Generated by Django 4.2.6 on 2023-12-09 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0034_rename_orderinvoicenumber_orderdetail_orderinvoiceno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfitAfterSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductCode', models.CharField(blank=True, max_length=10, null=True)),
                ('qty', models.IntegerField()),
                ('AvgCost', models.IntegerField()),
                ('SalePrice', models.IntegerField()),
                ('Profit', models.IntegerField()),
                ('i_dt', models.DateTimeField(auto_now=True)),
                ('i_usr', models.CharField(max_length=150)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_adminPanel.products')),
                ('SaleInvoiceNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_adminPanel.salemaster')),
            ],
            options={
                'verbose_name_plural': 'ProfitAfterSale',
            },
        ),
    ]
