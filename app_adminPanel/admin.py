from django.contrib import admin
from .models import Brand, Category, Color, Size, Supplier, Division, District, Thana, Area, CustomerShippingAddress
from .models import Products, ProductDetail, ProductMultipleImage, PurchaseDetail, OrderMaster, OrderDetail
from .models import SaleMaster, SaleHistory, ReturnMaster, ReturnDetail, WishList, CustomerLoginHistory
# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'BrandName')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'CategoryName','BrandId')

class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'ColorName')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'SizeName','Brand','Category')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'SupplierName')

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'divisionName')

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'DistrictName', 'Division', 'DivisionName')

class ThanaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ThanaName', 'DistrictName', 'DivisionName')

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'AreaName', 'Thana', 'District', 'Division')

class CustomerShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'Customername', 'MobileNumber', 'Email', 
                    'Address1', 'Address2', 'District', 'Thana', 'Area')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProductCode', 'ProductName', 'UnitPurchasePrice', 'UnitCurrSalePrice', 'UnitOldSalePrice', 
                    'UnitStockInHand', 'Brand','Category', 'Size', 'Image', 'productDesc')

class ProductDetailtAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProductCode', 'PreviousStock', 'UnitPurchasePrice', 'UnitCurrSalePrice', 'UnitOldSalePrice', 
                    'StockInHand', 'Color','Size','Image')

class ProductMultipleImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'Product', 'Images')
    
class PurchaseMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'PurchaseInvoiceNo', 'PurchaseQty', 'UnitPurchasePrice',
                     'TotalPurchasePrice', 'Supplier')

class PurchaseDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'PurInvoice', 'Product', 'Productdtl', 'ProductCode', 'Qty',
                     'UnitPurchasePrice', 'totalPurchasePrice', 'UnitCurrSalePrice', 'Supplier')

class OrderMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'OrderInvoiceNo', 'Product', 'Qty', 'TotalPurchasePrice',
                     'PurchasePrice', 'OldSalePrice', 'CurrSalePrice', 
                     'TotalSalePrice', 'SepcialDiscount', 'TotalPrice', 
                     'BrandName', 'CategoryName', 'ColorName','SizeName', 'Customer', 'ProductDeliveryStatus')

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'OrderInvoiceNo', 'Product', 'UnitQty', 'UnitPurchasePrice',
                     'UnitCurrSalePrice', 'UnitOldSalePrice', 'TotalSalePrice', 
                     'BrandName', 'CategoryName', 'ColorName','SizeName', 'Customername')
    
class SaleMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'SaleInvoiceNo', 'Product', 'Qty', 'TotalPurchasePrice',
                     'PurchasePrice', 'OldSalePrice', 'CurrSalePrice', 
                     'TotalSalePrice', 'SepcialDiscount', 'TotalPrice', 
                     'BrandName', 'CategoryName', 'ColorName','SizeName', 'Customer', 'ProductDeliveryStatus')

class SaleHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'SaleInvoiceNo', 'Product', 'UnitQty', 'UnitPurchasePrice',
                     'UnitCurrSalePrice', 'UnitOldSalePrice', 'TotalSalePrice', 
                     'BrandName', 'CategoryName', 'ColorName','SizeName', 'Customername')

class ReturnMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'SaleInvoiceNo', 'Product', 'UnitQty',
                     'UnitCurrSalePrice', 'TotalSalePrice', 'SepcialDiscount', 'TotalPrice',
                     'BrandName', 'CategoryName', 'ColorName','SizeName', 'Customer', 'ProductDeliveryStatus')

class ReturnDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'SaleInvoiceNo', 'Product', 'UnitQty', 'UnitPurchasePrice',
                     'UnitCurrSalePrice', 'UnitOldSalePrice', 'TotalSalePrice',
                     'BrandName', 'CategoryName', 'ColorName','SizeName', 'Customer')

class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'Product', 'UnitQty')

class CustomerLoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Customer', 'LogingTime', 'LogOutTime')

# class CustomerLoginHistory(models.Model):
# 	Customer	    	= models.ForeignKey(CustomerShippingAddress,on_delete=models.CASCADE)
# 	LogingTime	    	= models.DateTimeField(auto_now=True)
# 	LogOutTime		    = models.DateTimeField(auto_now=True)
# 	class Meta:
# 		verbose_name_plural = 'CustomerLoginHistory'

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Thana, ThanaAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(CustomerShippingAddress, CustomerShippingAddressAdmin)
admin.site.register(ProductDetail, ProductDetailtAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductMultipleImage, ProductMultipleImgAdmin)
admin.site.register(PurchaseDetail, PurchaseDetailAdmin)
admin.site.register(OrderMaster, OrderMasterAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(SaleMaster, SaleMasterAdmin)
admin.site.register(SaleHistory, SaleHistoryAdmin)
admin.site.register(ReturnMaster, ReturnMasterAdmin)
admin.site.register(ReturnDetail, ReturnDetailAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(CustomerLoginHistory, CustomerLoginHistoryAdmin)
