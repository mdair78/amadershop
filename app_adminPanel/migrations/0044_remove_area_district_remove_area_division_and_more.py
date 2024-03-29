# Generated by Django 4.2.6 on 2023-12-11 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_adminPanel', '0043_alter_products_brand_alter_products_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='District',
        ),
        migrations.RemoveField(
            model_name='area',
            name='Division',
        ),
        migrations.RemoveField(
            model_name='area',
            name='Thana',
        ),
        migrations.RemoveField(
            model_name='avgpurchasecost',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='customerloginhistory',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='customershippingaddress',
            name='Area',
        ),
        migrations.RemoveField(
            model_name='customershippingaddress',
            name='District',
        ),
        migrations.RemoveField(
            model_name='customershippingaddress',
            name='Division',
        ),
        migrations.RemoveField(
            model_name='customershippingaddress',
            name='Thana',
        ),
        migrations.RemoveField(
            model_name='district',
            name='Division',
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='Color',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='Customername',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='OrderInvoiceNo',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='ProductCode',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='ordermaster',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='ordermaster',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='ordermaster',
            name='Color',
        ),
        migrations.RemoveField(
            model_name='ordermaster',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='ordermaster',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='ordermaster',
            name='ProductCode',
        ),
        migrations.RemoveField(
            model_name='ordermaster',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='proddtl',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='proddtl',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='Color',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='productmultipleimage',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='productmultipleimage',
            name='ProductCode',
        ),
        migrations.RemoveField(
            model_name='products',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='products',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='profitaftersale',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='profitaftersale',
            name='SaleInvoiceNo',
        ),
        migrations.RemoveField(
            model_name='purchasedetail',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='purchasedetail',
            name='Productdtl',
        ),
        migrations.RemoveField(
            model_name='purchasedetail',
            name='PurchaseMaster',
        ),
        migrations.RemoveField(
            model_name='purchasedetail',
            name='Supplier',
        ),
        migrations.RemoveField(
            model_name='purchasemaster',
            name='Supplier',
        ),
        migrations.RemoveField(
            model_name='returndetail',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='returndetail',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='returndetail',
            name='Color',
        ),
        migrations.RemoveField(
            model_name='returndetail',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='returndetail',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='returndetail',
            name='ProductCode',
        ),
        migrations.RemoveField(
            model_name='returndetail',
            name='SaleInvoiceNo',
        ),
        migrations.RemoveField(
            model_name='returndetail',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='returnmaster',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='returnmaster',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='returnmaster',
            name='Color',
        ),
        migrations.RemoveField(
            model_name='returnmaster',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='returnmaster',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='returnmaster',
            name='ProductCode',
        ),
        migrations.RemoveField(
            model_name='returnmaster',
            name='SaleInvoiceNo',
        ),
        migrations.RemoveField(
            model_name='returnmaster',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='salehistory',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='salehistory',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='salehistory',
            name='Color',
        ),
        migrations.RemoveField(
            model_name='salehistory',
            name='Customername',
        ),
        migrations.RemoveField(
            model_name='salehistory',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='salehistory',
            name='ProductCode',
        ),
        migrations.RemoveField(
            model_name='salehistory',
            name='SaleInvoiceNo',
        ),
        migrations.RemoveField(
            model_name='salehistory',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='salemaster',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='salemaster',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='salemaster',
            name='Color',
        ),
        migrations.RemoveField(
            model_name='salemaster',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='salemaster',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='salemaster',
            name='ProductCode',
        ),
        migrations.RemoveField(
            model_name='salemaster',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='size',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='size',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='thana',
            name='District',
        ),
        migrations.RemoveField(
            model_name='thana',
            name='Division',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='ProductCode',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='AvgPurchaseCost',
        ),
        migrations.DeleteModel(
            name='CustomerLoginHistory',
        ),
        migrations.DeleteModel(
            name='CustomerShippingAddress',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Division',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
        migrations.DeleteModel(
            name='OrderMaster',
        ),
        migrations.DeleteModel(
            name='proddtl',
        ),
        migrations.DeleteModel(
            name='ProductDetail',
        ),
        migrations.DeleteModel(
            name='ProductMultipleImage',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='ProfitAfterSale',
        ),
        migrations.DeleteModel(
            name='PurchaseDetail',
        ),
        migrations.DeleteModel(
            name='PurchaseMaster',
        ),
        migrations.DeleteModel(
            name='ReturnDetail',
        ),
        migrations.DeleteModel(
            name='ReturnMaster',
        ),
        migrations.DeleteModel(
            name='SaleHistory',
        ),
        migrations.DeleteModel(
            name='SaleMaster',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='Thana',
        ),
        migrations.DeleteModel(
            name='WishList',
        ),
    ]
