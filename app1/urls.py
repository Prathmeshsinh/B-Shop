
from django.urls import path
# from app1.views import data,index,productall
from app1.views import *

urlpatterns = [
    path('data/',data),
    path('',index,name="home"),
    path('product-all/',productall,name='productall'),
    path('product-filter/<int:id>/',productfilter,name='product_filter'),
    path('product-get/<int:id>',productget,name="product_get"),
    path('login/',login,name="login1"),
    path('logout/',logout,name='logout1'),
    path('register/',register,name="register1"),
    path('profile/',profile,name="profile1"),
    path('Change-Password/',changepass,name="changepass"),
    path('Vendor-login/',vendorlogin,name="Vendorlogin"),
    path('vendor-register/',vendorregister,name='vendorregister'),
    path('vendor-logout/',vendorlogout,name="vendorlogout"),
    path('contactus/',contactus,name="contactus1"),
    path('add_product/',add_product,name="addproduct"),
    path('update-product/<int:id>/',updateproduct,name="updateproduct1"),
    path('add-cart/',addcart,name="addtocart123"),
    path('cart/',cartpage,name="cart2"),
    path('removeitem/<int:id>',removeitem,name="removeitem1"),
    path('removeallitem/',removeallitem,name="removeallitem1"),
    path('shipping/',shipping ,name="shipping1"),
    path('success/',success ,name="success1"),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('order-table/',ordertable,name="myorder"),
    path('order-details/<int:id>/',orderdetails,name="orderdetails2"),
    path('vendororder/',vendor_order,name="vendororder"),
    path('search/',productsearch,name='search')
] 