from django.contrib import admin
from .models import *

# Register your models here.
class userregister(admin.ModelAdmin):
    list_display=['username','useremail','usercontactno','usergender','user_DOB',]
admin.site.register(UserRegister,userregister)

class vendorregister(admin.ModelAdmin):
    list_display=['vendorname','vendoremail','vendorcontactno','vendor_DOB',]
admin.site.register(VendorRegister,vendorregister)

class Contactregister(admin.ModelAdmin):
    list_display=['name','email']
admin.site.register(Contactus,Contactregister)

class hotelregister(admin.ModelAdmin):
    list_display=['vendorId','place_name','city','state','contact_number']
admin.site.register(hotel,hotelregister)

class Paymentdetails(admin.ModelAdmin):
    list_display=['user','Owner','hotel_name','PaymentMethod','Amount','orderDate']
admin.site.register(pymentdetails,Paymentdetails)