from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

# Parameter Table
# 01. Brand
# 02. Categroy
# 03. Colors
# 04. Size
# 05. Supplier
# 06. Division
# 07. District
# 08. Thana
# 09. Area
# 10. CustomerShippingAddress
# 11. UserAdmin

# Transaction Table
# 01. Products
# 02. ProductDetail
# 03. ProductMultipleImage
# 04. PurchaseMaster
# 05. PurchaseDetail
# 06. SaleMaster
# 07. SaleHistory
# 08. ReturnMaster
# 09. ReturnDetail
# 10. WishList
# 11. CustomerLoginHistory

class Brand(models.Model):
	BrandName		    = models.CharField(max_length=100)
	class Meta:
		verbose_name_plural = 'Brand'
	def __str__(self) -> str:
		return f"{self.id} {self.BrandName}"

class Category(models.Model):
	CategoryName		= models.CharField(max_length=100)
	BrandId			    = models.ForeignKey(Brand,on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural = 'Category'		
	# def __str__(self) -> str:
	# 	return f"{self.BrandId} {self.id} {self.CategoryName}"

class Color(models.Model):
	ColorName	    	= models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = 'Color'
	def __str__(self) -> str:
		return f"{self.id} {self.ColorName}"		

class Size(models.Model):
	SizeName	    	= models.CharField(max_length=50, blank=True, null=True)
	Brand			    = models.ForeignKey(Brand,on_delete=models.CASCADE, blank=True, null=True)
	Category		    = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'Size'
	def __str__(self) -> str:
		return f"{self.id} {self.SizeName}"	
	
class Supplier(models.Model):
	SupplierName		= models.CharField(max_length=100)
	class Meta:
		verbose_name_plural = 'Supplier'
	def __str__(self) -> str:
		return f"{self.id} {self.SupplierName}"	

class Division(models.Model):
	divisionCode		= models.IntegerField(blank=True, null=True)
	divisionName		= models.CharField(max_length=100, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'Division'
	def __str__(self) -> str:
		return f"{self.id} {self.divisionName}"	

class District(models.Model):
	DistrictCode		= models.IntegerField(blank=True, null=True)
	DistrictName		= models.CharField(max_length=100, blank=True, null=True)
	Division			= models.ForeignKey(Division,on_delete=models.CASCADE, blank=True, null=True)
	DivisionName		= models.CharField(max_length=100, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'District'
	def __str__(self) -> str:
		return f"{self.id} {self.DistrictName}"	

class Thana(models.Model):
	ThanaCode			= models.IntegerField(blank=True, null=True)
	ThanaName	    	= models.CharField(max_length=200, blank=True, null=True)
	District		    = models.ForeignKey(District,on_delete=models.CASCADE, blank=True, null=True)
	DistrictName		= models.CharField(max_length=100, blank=True, null=True)
	Division			= models.ForeignKey(Division,on_delete=models.CASCADE, blank=True, null=True)
	DivisionName		= models.CharField(max_length=100, blank=True, null=True)
	deviveryCharge		= models.IntegerField(blank=True, null=True)
	class Meta:
		verbose_name_plural = 'Thana'
	def __str__(self) -> str:
		return f"{self.id} {self.ThanaName}"	

class Area(models.Model):
	AreaName    		= models.CharField(max_length=100, blank=True, null=True)
	District	    	= models.ForeignKey(District,on_delete=models.CASCADE, blank=True, null=True)
	Thana		    	= models.ForeignKey(Thana,on_delete=models.CASCADE, blank=True, null=True)
	Division			= models.ForeignKey(Division,on_delete=models.CASCADE, blank=True, null=True)
	# DivisionName		= models.CharField(max_length=100, blank=True, null=True)
	deviveryCharge		= models.IntegerField(blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Area'
	def __str__(self) -> str:
		return f"{self.id} {self.AreaName}"	

class CustomerShippingAddress(models.Model):
	Customername		= models.CharField(max_length=50, blank=True, null=True)
	MobileNumber		= models.CharField(max_length=11, blank=True, null=True)
	Email		    	= models.CharField(max_length=100, blank=True, null=True)
	Address1	    	= models.CharField(max_length=200, blank=True, null=True)
	Address2	    	= models.CharField(max_length=200, blank=True, null=True)
	Division	    	= models.ForeignKey(Division,on_delete=models.CASCADE, blank=True, null=True)
	DivisionName	    = models.CharField(max_length=100, blank=True, null=True)
	District	    	= models.ForeignKey(District,on_delete=models.CASCADE, blank=True, null=True)
	DistrictName	    = models.CharField(max_length=100, blank=True, null=True)
	Thana		    	= models.ForeignKey(Thana,on_delete=models.CASCADE, blank=True, null=True)
	ThanaName	   		= models.CharField(max_length=100, blank=True, null=True)
	Area		    	= models.ForeignKey(Area,on_delete=models.CASCADE, blank=True, null=True)
	AreaName	   		 = models.CharField(max_length=100, blank=True, null=True)
	i_dt		    	= models.DateTimeField(auto_now=True)
	u_dt		    	= models.DateTimeField(auto_now_add=True, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'CustomerShippingAddress'
	def __str__(self) -> str:
		return f"{self.id} {self.Customername}"	

# class User(AbstractUser):
#     user_type          = models.IntegerField(default=1)
#     user_roll          = models.IntegerField(blank=True, null=True)
#     login_time         = models.DateTimeField(auto_now=True)
#     userImage          = models.ImageField(upload_to='userImage/', blank=True, null=True)

# class UserCustom(AbstractUser): # In app_website I cannot create UserCustom. I setup permission though showing HINT: Add or change a related_name argument to the definition for 'app_website.UserCustom.user_permissions' or 'app_adminPanel.User.user_permissions'.
# 	user_type	    	= models.IntegerField(default=1)
# 	user_roll	    	= models.IntegerField(blank=True, null=True)
# 	login_time	    	= models.IntegerField(blank=True, null=True)
# 	userImage	    	= models.ImageField(upload_to='userImage/', blank=True, null=True)

class Products(models.Model):
	ProductCode	    	= models.CharField(max_length=10, blank=True, null=True)
	ProductName	    	= models.CharField(max_length=100, blank=True, null=True)
	Brand			    = models.ForeignKey(Brand,on_delete=models.CASCADE, blank=True, null=True)
	Category	    	= models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
	Size		    	= models.ForeignKey(Size,on_delete=models.CASCADE, blank=True, null=True)
	UnitPurchasePrice	= models.IntegerField(blank=True, null=True)	# Update When Purchase new products
	UnitCurrSalePrice	= models.IntegerField(blank=True, null=True)	# Update When Purchase new products
	UnitOldSalePrice	= models.IntegerField(blank=True, null=True)	# Update When Purchase new products
	UnitStockInHand		= models.IntegerField(blank=True, null=True)	# Update When Purchase new products (Auto Calculate)
	Image		    	= models.ImageField(upload_to='product_image/', blank=True, null=True)
	productDesc			= models.TextField()
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	u_dt		    	= models.DateTimeField(auto_now_add=True)
	u_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'Products'
	def __str__(self) -> str:
		return f"{self.id} {self.ProductName}"

class ProductDetail(models.Model):
	Product		    	= models.ForeignKey(Products,on_delete=models.CASCADE, blank=True, null=True)
	ProductCode	    	= models.CharField(max_length=10, blank=True, null=True)
	PreviousStock		= models.IntegerField(blank=True, null=True)	# Update with UnitStockInHand column When Purchase new products
	UnitPurchasePrice	= models.IntegerField(blank=True, null=True)	# Update When Purchase new products
	UnitCurrSalePrice	= models.IntegerField(blank=True, null=True)	# Update When Purchase new products
	UnitOldSalePrice	= models.IntegerField(blank=True, null=True)	# Update When Purchase new products
	StockInHand			= models.IntegerField(blank=True, null=True)	# Update When Purchase new products
	Color		    	= models.ForeignKey(Color,on_delete=models.CASCADE, blank=True, null=True)
	Size		    	= models.ForeignKey(Size,on_delete=models.CASCADE, blank=True, null=True)
	Image		    	= models.ImageField(upload_to='product_images/')
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	u_dt		    	= models.DateTimeField(auto_now_add=True, blank=True, null=True)
	u_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'ProductDetail'
	# def __str__(self) -> str:
	# 	return f"{self.id} {self.ProductName}"

class ProductMultipleImage(models.Model):
	Product		    	= models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
	ProductCode	    	= models.ForeignKey(Products,on_delete=models.CASCADE)
	Images	    		= models.ImageField(upload_to='product_multi_image/')
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	u_dt		    	= models.DateTimeField(auto_now_add=True)
	u_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'ProductMultipleImage'
	def __str__(self) -> str:
		return f"{self.id} {self.ProductName}"

class Invoice(models.Model):					# Only Total Purchase cost will be insert in this model
	PurInvoiceNo		= models.CharField(max_length=10, blank=True, null=True)	# Incremental IntegerFieldField + dd + mm + yy 
	PurchaseQty		    = models.IntegerField() # All Items will be sum (Like: Socks 500 + Cap 50 + Passport Holder 50 = Total Qty 600)
	PurchasePrice		= models.IntegerField() # All Items will be sum (Like: Socks + Cap + Passport Holder = TotalPurchasePrice)
	Suppli	    		= models.ForeignKey(Supplier,on_delete=models.CASCADE, blank=True, null=True)
	InvoiceDate			= models.DateField(blank=True, null=True)
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'Invoice'

class PurchaseDetail(models.Model): # Purchase Cost Price will be calculate from here. 
	# Product Name and Image Must be shown here from productDetail Table
	PurInvoice			= models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=True, null=True)
	Product 			= models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
	# PurchaseMaster 		= models.ForeignKey(PurchaseMaster, on_delete=models.CASCADE, blank=True, null=True)
	# PurchaseInvoiceNo	= models.CharField(max_length=12)
	Productdtl		    = models.ForeignKey(ProductDetail,on_delete=models.CASCADE, blank=True, null=True)
	ProductCode	    	= models.CharField(max_length=10, blank=True, null=True)
	Qty		 		   	= models.IntegerField() 
	UnitPurchasePrice	= models.IntegerField()
	totalPurchasePrice	= models.IntegerField()
	UnitCurrSalePrice	= models.IntegerField() # No need here
	Supplier	    	= models.ForeignKey(Supplier,on_delete=models.CASCADE, blank=True, null=True)
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'PurchaseDetail'

class AvgPurchaseCost(models.Model): 
	Product		    	= models.ForeignKey(Products,on_delete=models.CASCADE, blank=True, null=True)
	ProductCode	    	= models.CharField(max_length=10, blank=True, null=True)
	StockInHand		    = models.IntegerField(blank=True, null=True) # Update When purchase
	AvgCost				= models.IntegerField(blank=True, null=True) # Update When purchase 
	# Stock 5 qty, cost 200Tk, then new purchase 20 qty, cost 220Tk 
	# Calculate: total stock 5*20 = 25 qty, total cost (5*200 = 1000Tk, new purchase 20*220 = 4400Tk) 1000+4400 = 5400 agvcost = 5400/25 
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	u_dt		    	= models.DateTimeField(auto_now=True)
	u_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'AvgPurchaseCost'
	

class OrderMaster(models.Model):
	OrderInvoiceNo		= models.CharField(max_length=150, blank=True, null=True)	# Incremental IntegerField + yy + mm + dd 
	Product		    	= models.ForeignKey(ProductDetail,on_delete=models.CASCADE, blank=True, null=True)
	ProductCode	    	= models.ForeignKey(Products,on_delete=models.CASCADE, blank=True, null=True)
	Qty		        	= models.IntegerField()
	TotalPurchasePrice	= models.IntegerField()			# Qty * PurchasePrice
	PurchasePrice		= models.IntegerField()
	OldSalePrice		= models.IntegerField()
	CurrSalePrice		= models.IntegerField()
	TotalSalePrice		= models.IntegerField()			# Qty * CurrSalePrice
	SepcialDiscount		= models.IntegerField()
	TotalPrice	    	= models.IntegerField()			# TotalSalePrice - SepcialDiscount
	Brand			    = models.ForeignKey(Brand,on_delete=models.CASCADE, blank=True, null=True)
	BrandName	    	= models.CharField(max_length=100, blank=True, null=True) 
	Category	    	= models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
	CategoryName	  	= models.CharField(max_length=100, blank=True, null=True) 
	Color		    	= models.ForeignKey(Color,on_delete=models.CASCADE, blank=True, null=True)
	ColorName		 	= models.CharField(max_length=100, blank=True, null=True) 
	Size		    	= models.ForeignKey(Size,on_delete=models.CASCADE, blank=True, null=True)
	SizeName	 	 	= models.CharField(max_length=100, blank=True, null=True) 
	Customer    		= models.ForeignKey(CustomerShippingAddress,on_delete=models.CASCADE, blank=True, null=True)
	ProductDeliveryStatus	= models.IntegerField(blank=True, null=True)	# Value - Full Deliverd, Partial Deliverd and Return
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150, blank=True, null=True)
	class Meta:
		verbose_name_plural = 'OrderMaster'
	def __str__(self) -> str:
		return f"{self.id} {self.ProductName}"	
	
class OrderDetail(models.Model):
	OrderInvoiceNo		= models.ForeignKey(OrderMaster,on_delete=models.CASCADE)
	Product		    	= models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
	ProductCode	    	= models.ForeignKey(Products,on_delete=models.CASCADE)
	UnitQty		    	= models.IntegerField() 
	UnitPurchasePrice	= models.IntegerField()
	UnitCurrSalePrice	= models.IntegerField()
	UnitOldSalePrice	= models.IntegerField()
	TotalSalePrice		= models.IntegerField()	# UnitQty * UnitCurrSalePrice
	Brand			    = models.ForeignKey(Brand,on_delete=models.CASCADE)
	BrandName	    	= models.CharField(max_length=100, blank=True, null=True) 
	Category	    	= models.ForeignKey(Category,on_delete=models.CASCADE)
	CategoryName	  	= models.CharField(max_length=100, blank=True, null=True) 
	Color		    	= models.ForeignKey(Color,on_delete=models.CASCADE)
	ColorName		 	= models.CharField(max_length=100, blank=True, null=True) 
	Size		    	= models.ForeignKey(Size,on_delete=models.CASCADE)
	SizeName	 	 	= models.CharField(max_length=100, blank=True, null=True) 
	Customername		= models.ForeignKey(CustomerShippingAddress,on_delete=models.CASCADE)
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150)
	class Meta:
		verbose_name_plural = 'OrderDetail'
	def __str__(self) -> str:
		return f"{self.id} {self.ProductName}"	

class SaleMaster(models.Model):
	SaleInvoiceNo	= models.CharField(max_length=150)	# Incremental IntegerField + yy + mm + dd 
	Product		    	= models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
	ProductCode	    	= models.ForeignKey(Products,on_delete=models.CASCADE)
	Qty		        	= models.IntegerField()
	TotalPurchasePrice	= models.IntegerField()			# Qty * PurchasePrice
	PurchasePrice		= models.IntegerField()
	OldSalePrice		= models.IntegerField()
	CurrSalePrice		= models.IntegerField()
	TotalSalePrice		= models.IntegerField()			# Qty * CurrSalePrice
	SepcialDiscount		= models.IntegerField()
	TotalPrice	    	= models.IntegerField()			# TotalSalePrice - SepcialDiscount
	Brand			    = models.ForeignKey(Brand,on_delete=models.CASCADE)
	BrandName	    	= models.CharField(max_length=100, blank=True, null=True) 
	Category	    	= models.ForeignKey(Category,on_delete=models.CASCADE)
	CategoryName	  	= models.CharField(max_length=100, blank=True, null=True) 
	Color		    	= models.ForeignKey(Color,on_delete=models.CASCADE)
	ColorName		 	= models.CharField(max_length=100, blank=True, null=True) 
	Size		    	= models.ForeignKey(Size,on_delete=models.CASCADE)
	SizeName	 	 	= models.CharField(max_length=100, blank=True, null=True) 
	Customer    		= models.ForeignKey(CustomerShippingAddress,on_delete=models.CASCADE)
	ProductDeliveryStatus	= models.IntegerField(blank=True, null=True)	# Value - Full Deliverd, Partial Deliverd and Return
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150)
	class Meta:
		verbose_name_plural = 'SaleMaster'
	def __str__(self) -> str:
		return f"{self.id} {self.ProductName}"	

class SaleHistory(models.Model):
	SaleInvoiceNo		= models.ForeignKey(SaleMaster,on_delete=models.CASCADE)
	Product		    	= models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
	ProductCode	    	= models.ForeignKey(Products,on_delete=models.CASCADE)
	UnitQty		    	= models.IntegerField() 
	UnitPurchasePrice	= models.IntegerField()
	UnitCurrSalePrice	= models.IntegerField()
	UnitOldSalePrice	= models.IntegerField()
	TotalSalePrice		= models.IntegerField()	# UnitQty * UnitCurrSalePrice
	Brand			    = models.ForeignKey(Brand,on_delete=models.CASCADE)
	BrandName	    	= models.CharField(max_length=100, blank=True, null=True) 
	Category	    	= models.ForeignKey(Category,on_delete=models.CASCADE)
	CategoryName	  	= models.CharField(max_length=100, blank=True, null=True) 
	Color		    	= models.ForeignKey(Color,on_delete=models.CASCADE)
	ColorName		 	= models.CharField(max_length=100, blank=True, null=True) 
	Size		    	= models.ForeignKey(Size,on_delete=models.CASCADE)
	SizeName	 	 	= models.CharField(max_length=100, blank=True, null=True) 
	Customername		= models.ForeignKey(CustomerShippingAddress,on_delete=models.CASCADE)
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150)
	class Meta:
		verbose_name_plural = 'SaleHistory'
	def __str__(self) -> str:
		return f"{self.id} {self.ProductName}"

class ProfitAfterSale(models.Model): 
	SaleInvoiceNo		= models.ForeignKey(SaleMaster,on_delete=models.CASCADE)
	Product		    	= models.ForeignKey(Products,on_delete=models.CASCADE)
	ProductCode	    	= models.CharField(max_length=10, blank=True, null=True)
	qty				    = models.IntegerField()
	AvgCost				= models.IntegerField() # Average Cost will be SaleHistory table PurchasePrice
	SalePrice			= models.IntegerField() # Sale Price will be SaleHistory table PurchasePrice
	Profit				= models.IntegerField() # SalePrice - AvgCost
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150)
	class Meta:
		verbose_name_plural = 'ProfitAfterSale'

class ReturnMaster(models.Model):
	SaleInvoiceNo	= models.ForeignKey(SaleMaster,on_delete=models.CASCADE)
	Product	    		= models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
	ProductCode	    	= models.ForeignKey(Products,on_delete=models.CASCADE)
	UnitQty		    	= models.IntegerField()
	UnitCurrSalePrice	= models.IntegerField()
	TotalSalePrice		= models.IntegerField()			# Qty * CurrSalePrice
	SepcialDiscount		= models.IntegerField()
	TotalPrice	    	= models.IntegerField()			# TotalSalePrice - SepcialDiscount
	Brand			    = models.ForeignKey(Brand,on_delete=models.CASCADE)
	BrandName	    	= models.CharField(max_length=100, blank=True, null=True) 
	Category	    	= models.ForeignKey(Category,on_delete=models.CASCADE)
	CategoryName	  	= models.CharField(max_length=100, blank=True, null=True) 
	Color		    	= models.ForeignKey(Color,on_delete=models.CASCADE)
	ColorName		 	= models.CharField(max_length=100, blank=True, null=True) 
	Size		    	= models.ForeignKey(Size,on_delete=models.CASCADE)
	SizeName	 	 	= models.CharField(max_length=100, blank=True, null=True) 
	Customer    		= models.ForeignKey(CustomerShippingAddress,on_delete=models.CASCADE)
	ProductDeliveryStatus	= models.IntegerField()			# Value - Full Return and Partial Return
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150)
	class Meta:
		verbose_name_plural = 'ReturnMaster'
	def __str__(self) -> str:
		return f"{self.id} {self.ProductName}"	

class ReturnDetail(models.Model):
	SaleInvoiceNo	= models.ForeignKey(SaleMaster,on_delete=models.CASCADE)
	Product			    = models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
	ProductCode	    	= models.ForeignKey(Products,on_delete=models.CASCADE)
	UnitQty		    	= models.IntegerField() 
	UnitPurchasePrice	= models.IntegerField()
	UnitCurrSalePrice	= models.IntegerField()
	UnitOldSalePrice	= models.IntegerField()
	TotalSalePrice		= models.IntegerField()			# UnitQty * UnitCurrSalePrice
	Brand			    = models.ForeignKey(Brand,on_delete=models.CASCADE)
	BrandName	    	= models.CharField(max_length=100, blank=True, null=True) 
	Category	    	= models.ForeignKey(Category,on_delete=models.CASCADE)
	CategoryName	  	= models.CharField(max_length=100, blank=True, null=True) 
	Color		    	= models.ForeignKey(Color,on_delete=models.CASCADE)
	ColorName		 	= models.CharField(max_length=100, blank=True, null=True) 
	Size		    	= models.ForeignKey(Size,on_delete=models.CASCADE)
	SizeName	 	 	= models.CharField(max_length=100, blank=True, null=True) 
	Customer    		= models.ForeignKey(CustomerShippingAddress,on_delete=models.CASCADE)
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150)
	class Meta:
		verbose_name_plural = 'ReturnDetail'
	def __str__(self) -> str:
		return f"{self.id} {self.ProductName}"	

class WishList(models.Model):
	Product		    	= models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
	ProductCode	    	= models.ForeignKey(Products,on_delete=models.CASCADE)
	UnitQty		    	= models.IntegerField() 
	i_dt		    	= models.DateTimeField(auto_now=True)
	i_usr		    	= models.CharField(max_length=150)
	class Meta:
		verbose_name_plural = 'WishList'
	def __str__(self) -> str:
		return f"{self.id} {self.ProductName}"	

class CustomerLoginHistory(models.Model):
	Customer	    	= models.ForeignKey(CustomerShippingAddress,on_delete=models.CASCADE)
	Customername		= models.CharField(max_length=50, blank=True, null=True)
	LogingTime	    	= models.DateTimeField(auto_now=True)
	LogOutTime		    = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name_plural = 'CustomerLoginHistory'


class proddtl(models.Model):
	Product		    	= models.ForeignKey(Products,on_delete=models.CASCADE)
	Size				= models.ForeignKey(Size,on_delete=models.CASCADE)
	purchaseprice		= models.IntegerField
	saleprice			= models.IntegerField




class MyModel(models.Model):
    key1 = models.CharField(max_length=255)
    key2 = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.key1} - {self.key2}'