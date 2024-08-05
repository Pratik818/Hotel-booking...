from django.db import models

# Create your models here.

class UserRegister(models.Model):
    username=models.CharField(max_length=20,default='',verbose_name='User Name')
    useremail=models.EmailField(max_length=50,verbose_name='Email',default=None)
    usercontactno=models.IntegerField(default='',verbose_name='Contact No')
    g = [
        (None, 'select gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    usergender=models.CharField(max_length=12,choices=g,default=None)
    userimage=models.ImageField(upload_to="user")
    user_DOB=models.DateField(default=None)
    user_address=models.TextField(default=None)
    userpassword=models.CharField(default=None,max_length=20,verbose_name='Password')
    
    def __str__(self):
        return self.username

class VendorRegister(models.Model):
    vendorname=models.CharField(max_length=20,default='',verbose_name='Vendor Name')
    vendoremail=models.EmailField(max_length=50,verbose_name='Email')
    vendorcontactno=models.IntegerField(default='',verbose_name='Contact No')
    company_address=models.TextField()
    vendorimage=models.ImageField(upload_to="Vendor",default=None)
    vendor_DOB=models.DateField(default=None)
    vendorpassword=models.CharField(max_length=20,verbose_name='Password')
    vendor_GST_no=models.CharField(max_length=50,verbose_name='Vendor GST No')
    
    def __str__(self):
        return self.vendorname

class Contactus(models.Model):
    name=models.CharField(max_length=20,default='',verbose_name=' Name')
    email=models.EmailField(max_length=50,verbose_name='Email')
    message=models.TextField()
    
    def __str__(self):
        return self.name

class hotel(models.Model):
    vendorId=models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    opentime=models.TimeField()
    closetime=models.TimeField()
    contact_number=models.IntegerField()
    description = models.TextField(default="")
    address=models.TextField(default="")
    price=models.IntegerField(default=0)
    productImage1 = models.ImageField(upload_to="product")
    productImage2 = models.ImageField(upload_to="product")
    productImage3 = models.ImageField(upload_to="product")
    productImage4 = models.ImageField(upload_to="product")
    ac  = models.BooleanField(default = False)

class pymentdetails(models.Model):
    userid=models.CharField(max_length=50)
    vendorid=models.CharField(max_length=50)
    hotelid=models.CharField(max_length=50)
    noofperson=models.CharField(max_length=50)
    user=models.CharField(max_length=50)
    Owner=models.CharField(max_length=50)
    hotel_name=models.CharField(max_length=50)
    PaymentVia=models.CharField(max_length=50)
    PaymentMethod=models.CharField(max_length=50)
    Amount=models.CharField(max_length=50)
    transactionId = models.TextField(default=None)
    cheackin=models.DateField()
    cheackout=models.DateField()
    orderDate = models.DateTimeField(auto_created=True,auto_now=True)
