from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('hotel/', Hotel, name='hotel'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addplace/', addplace, name='addplace'),
    path('yourdestination/', yourdestination, name='yourdestination'),
    path('blog/', blog, name='blog'),
    path('singleblog/', singleblog, name='singleblog'),
    path('singlehotel/<int:id>', singlehotel, name='singlehotel'),
    path('userlogin/', userlogin, name='userlogin'),
    path('userlogout/',userlogout,name='userlogout'),
    path('vendorlogin/', vendorlogin, name='vendorlogin'),
    path('vendorlogout/', vendorlogout, name='vendorlogout'),
    path('usersignup/', usersignup, name='usersignup'),
    path('vendorsignup/', vendorsignup, name='vendorsignup'),
    path('direct_buy/',paymentofbooking,name="paymentofbooking"),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('bookinghistory/', bookinghistory, name='bookinghistory'),
    
]