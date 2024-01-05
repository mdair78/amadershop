from django.shortcuts import render, redirect
from datetime import datetime
from app_adminPanel.models import Products, ProductDetail, Brand, Category, Size, Color, MyModel, Supplier, Invoice, PurchaseDetail
import os
from django.contrib import messages
from django.http import HttpResponse


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



def index(request):
    return render(request, 'adminPanel/index2.html')

# =======================================================New Products Entry ======================================================
def productentry(request):
    vBrand                  = Brand.objects.all()
    vCat                    = Category.objects.all()
    vSize                   = Size.objects.all()

    if request.method       == 'POST' and request.FILES:
        pCode               = request.POST.get('ProductCode')
        pName               = request.POST.get('ProductName')
        brand               = request.POST.get('Brand')
        cat                 = request.POST.get('Category')
        size                = request.POST.get('Size')
        UnitPurchasePrice   = request.POST.get('UnitPurchasePrice')
        UnitSalePrice       = request.POST.get('UnitSalePrice')
        ProductDesc         = request.POST.get('ProductDesc')
        ProductImage        = request.FILES['ProductImages']


        print(ProductImage)
        print(datetime.now())

        if size is None:
            productSave = Products(
                ProductCode          = pCode,
                ProductName          = pName,
                Brand_id             = brand,
                Category_id          = cat,
                UnitPurchasePrice    = UnitPurchasePrice,
                UnitCurrSalePrice    = UnitSalePrice,
                productDesc          = ProductDesc,           
                Image                = ProductImage,
    
            )
            productSave.save()
        else:
            productSave = Products(
                ProductCode          = pCode,
                ProductName          = pName,
                Brand_id             = brand,
                Category_id          = cat,
                Size_id              = size,
                UnitPurchasePrice    = UnitPurchasePrice,
                UnitCurrSalePrice    = UnitSalePrice,
                productDesc          = ProductDesc,           
                Image                = ProductImage,
    
            )
            productSave.save()

    # print(vBrand)

    return render(request, 'adminPanel/productentry.html', {'dBrand': vBrand, 'dCat': vCat, 'dSize': vSize})
    # return redirect('productShow', {'dBrand': vBrand, 'dCat': vCat, 'dSize': vSize})

# =======================================================End New Products Entry ==================================================


# =======================================================New Products Show =======================================================
def productShow(request):
    vProduct                     = Products.objects.all()

    return render(request, 'adminPanel/productshow.html', {'dProduct': vProduct})

def editProduct(request, id):
    vBrand                      = Brand.objects.all()
    vCat                        = Category.objects.all()
    vSize                       = Size.objects.all()

    vEdit = Products.objects.filter(id=id)
    return render(request, 'adminPanel/product-edit.html', {'dEdit': vEdit, 'dBrand': vBrand, 'dCat': vCat, 'dSize': vSize} )


# ======================================================= Products Update =======================================================
def updateProduct(request, id):
    if request.method       == 'POST' and request.FILES:
        pCode               = request.POST.get('ProductCode')
        pName               = request.POST.get('ProductName')
        brand               = request.POST.get('Brand')
        cat                 = request.POST.get('Category')
        size                = request.POST.get('Size')
        UnitPurchasePrice   = request.POST.get('UnitPurchasePrice')
        UnitSalePrice       = request.POST.get('UnitSalePrice')
        ProductDesc         = request.POST.get('ProductDesc')
        ProductImage        = request.FILES['ProductImages']

        productSave = Products.objects.filter(id = id)
        productSave = Products(
            id = id,
            ProductCode         = pCode,
            ProductName         = pName,
            Brand_id            = brand,
            Category_id         = cat,
            Size_id             = size,
            UnitPurchasePrice   = UnitPurchasePrice,
            UnitCurrSalePrice   = UnitSalePrice,
            productDesc         = ProductDesc,           
            Image               = ProductImage,
            u_dt                = datetime.now(),
        )
        productSave.save()
    else:
        pCode               = request.POST.get('ProductCode')
        pName               = request.POST.get('ProductName')
        brand               = request.POST.get('Brand')
        cat                 = request.POST.get('Category')
        size                = request.POST.get('Size')
        UnitPurchasePrice   = request.POST.get('UnitPurchasePrice')
        UnitSalePrice       = request.POST.get('UnitSalePrice')
        ProductDesc         = request.POST.get('ProductDesc')
        ProductImage        = request.POST.get('ProductImagesText')

        productSave = Products.objects.filter(id = id)
        productSave = Products(
            id = id,
            ProductCode         = pCode,
            ProductName         = pName,
            Brand_id            = brand,
            Category_id         = cat,
            Size_id             = size,
            UnitPurchasePrice   = UnitPurchasePrice,
            UnitCurrSalePrice   = UnitSalePrice,
            productDesc         = ProductDesc,           
            Image               = ProductImage,
            u_dt                = datetime.now(),
        )
        productSave.save()
    return redirect('productShow')
# =======================================================End Products Update ===================================================


# =======================================================Delete Product ========================================================
def deleteProduct(request, id):
    vDelete = Products.objects.filter(id=id).delete()
    return redirect('productShow')
# =======================================================End Delet Product =====================================================


# ======================================================= Products Detail Entry ================================================
def productdetail(request, id):
    vSize                       = Size.objects.all()
    vProd                       = Products.objects.filter(id=id)
    vColor                      = Color.objects.all()

    return render(request, 'adminPanel/productdtl.html', {'dProd': vProd, 'dColor': vColor, 'dSize': vSize} )

# ======================================================= Products Detail Add ================================================
def addProductDtlF(request):
    if request.method           == 'POST' and request.FILES:
        pId                     = request.POST.get('Product_id')
        pCode                   = request.POST.get('ProductCode')
        color                   = request.POST.get('color')
        size                    = request.POST.get('Size')
        vUnitPurchasePrice      = request.POST.get('UnitPurchasePrice')
        vUnitSalePrice          = request.POST.get('UnitSalePrice')
        vUnitOldSalePrice       = request.POST.get('UnitOldSalePrice')
        vUnitStockInHand        = request.POST.get('UnitStockInHand')
        ProductImage            = request.FILES['ProductImages']

        productDtlSave = ProductDetail(
            ProductCode         = pCode,
            Product_id          = pId,
            Color_id            = color,
            Size_id             = size,
            UnitPurchasePrice   = vUnitPurchasePrice,
            UnitCurrSalePrice   = vUnitSalePrice,
            UnitOldSalePrice    = vUnitOldSalePrice,
            StockInHand         = vUnitStockInHand,
            Image               = ProductImage,
            u_dt                = datetime.now(),
        )
        productDtlSave.save()
    return redirect('productShow')
# =======================================================End Products Update ===================================================


# ======================================================= Invoice Generate ======================================================
def invoicegen(request):
    vSupplierName           = Supplier.objects.all()

    if request.method       == 'POST':
        vinvoice            = request.POST.get('invoiceNo')
        vqty                = request.POST.get('PurchaseQty')
        vPrurPrice          = request.POST.get('PurchasePrice')
        vSupp               = request.POST.get('supplier')
        vSuppDt             = request.POST.get('invoiceDt')

        invoiceSave = Invoice(
            PurInvoiceNo      = vinvoice,
            PurchaseQty       = vqty,
            PurchasePrice     = vPrurPrice,
            Suppli_id         = vSupp, 
            InvoiceDate       = vSuppDt, 
        )
        invoiceSave.save()

    return render(request, 'adminPanel/invoiceGen.html', {'dSupplierName': vSupplierName})
# =======================================================End Invoice Generate ==================================================


# =======================================================Show Invoice ==========================================================
def showInvoice(request):
    vInvoice                    = Invoice.objects.all().order_by('-InvoiceDate').values()
    

    return render(request, 'adminPanel/invoiceshow.html', {'dInvoice' : vInvoice})

# =======================================================End Show Invoice ======================================================


# =======================================================Show Invoice ==========================================================
# shared_purInvoiceNo = None
def showproddtl(request, i_id):
    vProddtlAll             = ProductDetail.objects.all()
    vinvoic                 = Invoice.objects.filter(id=i_id)
    # request.session['vinvoic'] = vinvoic
    # global shared_purInvoiceNo


    purId                   = request.POST.get('purId')
    purInvoiceNo            = request.POST.get('purInvoiceNo')
    # shared_purInvoiceNo     = vinvoic

    print(purInvoiceNo)

    return render(request, 'adminPanel/product-detail-show.html', {'dProddtlAll' : vProddtlAll, 'dinvoic' : vinvoic, 'dpurInvoiceNo' : purInvoiceNo, 'dpurId' : purId})


# =======================================================End Show Invoice ======================================================

def purchase(request, id):
    vProductDtl                 = ProductDetail.objects.filter(id=id)
    vSize                       = Size.objects.all()
    vColor                      = Color.objects.all()
    vBrand                      = Brand.objects.all()
    vCat                        = Category.objects.all()

    # global shared_purInvoiceNo
    # if shared_purInvoiceNo is not None:
    #     print(shared_purInvoiceNo)
    #     print(shared_purInvoiceNo)
    #     print(shared_purInvoiceNo)

    return render(request, 'adminPanel/purchase.html', {'dProductDtl' : vProductDtl, 'dBrand' : vBrand, 'dCat' :vCat, 'dSize' : vSize, 'dColor' : vColor})


def purchaseSave(request, id):
    # if request.method           == 'POST':
    #     PurInvoice              = request.POST.get('ProductCode')
    #     Product_id              = request.POST.get('ProductName')
    #     Productdtl_id           = request.POST.get('Brand')
    #     ProductCode             = request.POST.get('Category')
    #     Qty                     = request.POST.get('Size')
    #     UnitPurchasePrice       = request.POST.get('UnitPurchasePrice')
    #     totalPurchasePrice      = request.POST.get('UnitSalePrice')
    #     UnitCurrSalePrice       = request.POST.get('ProductDesc')
    #     Supplier                = request.POST.get('ProductDesc')

    global shared_purInvoiceNo
    if shared_purInvoiceNo is not None:
        print(shared_purInvoiceNo)
        print(shared_purInvoiceNo)
        # print('shared_purInvoiceNo')
        # print('shared_purInvoiceNo')
        # print('shared_purInvoiceNo')
        # print('shared_purInvoiceNo')

        # v_purchaseSave = PurchaseDetail(
        #     ProductCode         = PurInvoice,
        #     Product_id          = Product_id,
        #     Productdtl_id       = Productdtl_id,
        #     # ProductCode         = ProductCode,
        #     Qty                 = Qty,
        #     UnitPurchasePrice   = UnitPurchasePrice,
        #     totalPurchasePrice  = totalPurchasePrice,
        #     UnitCurrSalePrice   = UnitCurrSalePrice,           
        #     Supplier            = Supplier,
        #     i_dt                = datetime.now(),
        # )
        # v_purchaseSave.save()
    
    return redirect('showproddtl', id=id) 


# def productShow(request):
#     vProduct                     = Products.objects.all()

#     return render(request, 'adminPanel/productshow.html', {'dProduct': vProduct})

# def editProduct(request, id):
#     vBrand                      = Brand.objects.all()
#     vCat                        = Category.objects.all()
#     vSize                       = Size.objects.all()

#     vEdit = Products.objects.filter(id=id)
#     return render(request, 'adminPanel/product-edit.html', {'dEdit': vEdit, 'dBrand': vBrand, 'dCat': vCat, 'dSize': vSize} )