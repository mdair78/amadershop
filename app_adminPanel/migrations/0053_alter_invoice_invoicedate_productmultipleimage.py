# Generated by Django 4.2.6 on 2023-12-12 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0052_mymodel_wishlist_returndetail_proddtl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='InvoiceDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='ProductMultipleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Images', models.ImageField(upload_to='product_multi_image/')),
                ('i_dt', models.DateTimeField(auto_now=True)),
                ('i_usr', models.CharField(blank=True, max_length=150, null=True)),
                ('u_dt', models.DateTimeField(auto_now_add=True)),
                ('u_usr', models.CharField(blank=True, max_length=150, null=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_adminPanel.productdetail')),
                ('ProductCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_adminPanel.products')),
            ],
            options={
                'verbose_name_plural': 'ProductMultipleImage',
            },
        ),
    ]