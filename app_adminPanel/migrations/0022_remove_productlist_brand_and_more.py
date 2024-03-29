# Generated by Django 4.2.6 on 2023-11-17 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0021_area_division_area_deviverycharge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlist',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='BrandName',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='CategoryName',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='ColorName',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='ProductName',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='SizeName',
        ),
        migrations.AlterField(
            model_name='productlist',
            name='Image',
            field=models.ImageField(upload_to='product_images/'),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductCode', models.CharField(max_length=8)),
                ('ProductName', models.CharField(max_length=100)),
                ('UnitPurchasePrice', models.IntegerField(blank=True, null=True)),
                ('UnitCurrSalePrice', models.IntegerField(blank=True, null=True)),
                ('UnitOldSalePrice', models.IntegerField(blank=True, null=True)),
                ('UnitStockInHand', models.IntegerField(blank=True, null=True)),
                ('Image', models.ImageField(upload_to='product_image/')),
                ('productDesc', models.TextField()),
                ('i_dt', models.DateTimeField(auto_now=True)),
                ('i_usr', models.CharField(max_length=150)),
                ('u_dt', models.DateTimeField(auto_now_add=True)),
                ('u_usr', models.CharField(max_length=150)),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_adminPanel.brand')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_adminPanel.category')),
                ('Size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_adminPanel.size')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AlterField(
            model_name='productlist',
            name='ProductCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_adminPanel.products'),
        ),
    ]
