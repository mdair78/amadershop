from django.urls import path
from app_adminPanel.views import parameter_views

urlpatterns = [
    path('', parameter_views.index, name='home'),

    # Product Entry, Show, Update, Delete
    path('productentry', parameter_views.productentry, name='productentry'),
    path('productShow', parameter_views.productShow, name='productShow'),
    path('showproddtl/<int:i_id>', parameter_views.showproddtl, name='showproddtl'),
    # path('showproddtl/<int:id>', parameter_views.showproddtl, name='showproddtl'),
    path('edit/<int:id>', parameter_views.editProduct, name='editproduct'),
    path('updateProduct/<int:id>', parameter_views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:id>', parameter_views.deleteProduct, name='deleteProduct'),
    
    # Detail Product Entry
    path('productdtl/<int:id>', parameter_views.productdetail, name='productdtl'),
    path('addProductDtl', parameter_views.addProductDtlF , name='addProductDtl'),
    
    # Product Purchase
    path('invoiceGen', parameter_views.invoicegen, name='invoiceGen'),
    path('showInvoice', parameter_views.showInvoice, name='showInvoice'),
        
    path('purchase/<int:id>', parameter_views.purchase, name='purchase'),
    path('purchaseSave/<int:id>', parameter_views.purchaseSave, name='purchaseSave'),

]