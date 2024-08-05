from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.session.has_key('user'):  
        print("index page for userrrrrr!!")     
        user= request.session['user']
        print(user,"userrrrrrrrrrrrrrr")
        data=UserRegister.objects.get(useremail=user)
        hotelDetails=hotel.objects.all()
        return render (request,'index.html',{'sessionuser':user,'name':data,'hotelDetails':hotelDetails})
    elif request.session.has_key('vendor'):
        print("index page for vendorrrrr!!")     
        vendor= request.session['vendor']
        hotelDetails=hotel.objects.filter(vendorId=request.session['vendorId'])
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'index.html',{'sessionvendor':vendor,'name':data,'hotelDetails':hotelDetails})
    else:
        print("index page")     
        hotelDetails=hotel.objects.all()
        return render (request,'index.html',{'hotelDetails':hotelDetails})


def usersignup(request):
    if request.method=='POST':
            model=UserRegister()
            model.username=request.POST['name']
            model.useremail=request.POST['email']
            model.usercontactno=request.POST['contact']
            model.user_address=request.POST['address']
            model.userimage=request.POST['image']
            model.user_DOB=request.POST['DOB']
            model.userpassword=request.POST['password']
            model.usergender=request.POST['gender']
            # print(model.usergender)
            model.save()
            return redirect('userlogin')
    return render(request,'usersignup.html')

def vendorsignup(request):
        if request.method=='POST':
            model=VendorRegister()
            model.vendorname=request.POST['name']
            model.vendoremail=request.POST['email']
            model.vendorcontactno=request.POST['contact']
            model.company_address=request.POST['address']
            model.vendorimage=request.POST['image']
            model.vendor_DOB=request.POST['DOB']
            model.vendorpassword=request.POST['password']
            model.vendor_GST_no=request.POST['GST_No']
            model.save()
            return redirect('vendorlogin')
        return render(request,'vendorsignup.html')

def Hotel(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        data1=hotel.objects.all()
        return render (request,'hotel.html',{'sessionuser':user,'name':data,'data':data1})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        data1=hotel.objects.filter(vendorId=request.session['vendorId'])
        return render (request,'hotel.html',{'sessionvendor':vendor,'name':data,'data':data1})
    else:
        data1=hotel.objects.all()
        return render (request,'hotel.html',{'data':data1})  #show data jyaare search kari ro a data ekhay j serch kary nahi to else ma all data dekhay

def about(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'about.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'about.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'about.html')

def contact(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        if request.method=="POST":
            model=Contactus()
            model.name=request.POST['name']
            model.email=request.POST['email']
            model.message=request.POST['message']
            model.save()
            return render (request,'contact.html',{'sessionuser':user,'name':data,'messagekey':'message sent'})
        return render (request,'contact.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        if request.method=="POST":
            model=Contactus()
            model.name=request.POST['name']
            model.email=request.POST['email']
            model.message=request.POST['message']
            model.save()
            return render (request,'contact.html',{'sessionvendor':vendor,'name':data,'messagekey':'message sent'})
        return render (request,'contact.html',{'sessionvendor':vendor,'name':data})
    else:
        if request.method=="POST":
            model=Contactus()
            model.name=request.POST['name']
            model.email=request.POST['email']
            model.message=request.POST['message']
            model.save()
            return render (request,'contact.html',{'messagekey':'message sent'})
        return render (request,'contact.html')

def addplace(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'addplace.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        if request.method=="POST" and request.FILES['productImage1']:
            model=hotel()
            model.vendorId=request.session['vendorId']
            model.place_name=request.POST['place_name']
            model.city=request.POST['city']
            model.state=request.POST['state']
            model.opentime=request.POST['opentime']
            model.closetime=request.POST['closetime']
            model.contact_number=request.POST['contact_number']
            model.description=request.POST['description']
            model.address=request.POST['address']
            model.price=request.POST['price']
            model.productImage1=request.FILES['productImage1']
            model.productImage2=request.FILES['productImage2']
            model.productImage3=request.FILES['productImage3']
            model.productImage4=request.FILES['productImage4']
            model.save()

        return render (request,'addplace.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'addplace.html')

def yourdestination(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        hoteldata=hotel.objects.all()
        stateset=set()
        cityset=set()
        placeset=set()
        for  i in hoteldata:
            stateset.add(i.state)
            cityset.add(i.city)
            placeset.add(i.place_name)
        statelist=list(stateset)
        citylist=list(cityset)
        placelist=list(placeset)
        if request.POST:
            query1 = request.POST['state']
            query2 = request.POST['city']
            query3 = request.POST['place']
            qset = [query1,query2,query3]
            print(qset)
            for q in qset:
                b = hotel.objects.filter(Q(place_name__icontains=q) | Q(
                    city__icontains=q) | Q(state__icontains=q)).distinct()
        
            return render(request, 'yourdestination.html', {'statelist':statelist,'citylist':citylist,'placelist':placelist,'sessionuser':user,'name':data,'hoteldata':hoteldata,'productdata': b,'p':query1,'q':query2,'r':query3})        
        return render(request, 'yourdestination.html', {'statelist':statelist,'citylist':citylist,'placelist':placelist,'sessionuser':user,'name':data,'hoteldata':hoteldata})
    else:
        hoteldata=hotel.objects.all()
        stateset=set()
        cityset=set()
        placeset=set()
        for  i in hoteldata:
            stateset.add(i.state)
            cityset.add(i.city)
            placeset.add(i.place_name)
        statelist=list(stateset)
        citylist=list(cityset)
        placelist=list(placeset)
        if request.POST:
            query1 = request.POST['state']
            query2 = request.POST['city']
            query3 = request.POST['place']
            qset = [query1,query2,query3]
            print(qset)
            for q in qset:
                b = hotel.objects.filter(Q(place_name__icontains=q) | Q(
                    city__icontains=q) | Q(state__icontains=q)).distinct()
            return render(request, 'yourdestination.html',{'statelist':statelist,'citylist':citylist,'placelist':placelist,'hoteldata':hoteldata,'productdata': b,'p':query1,'q':query2,'r':query3})
        return render (request,'yourdestination.html',{'statelist':statelist,'citylist':citylist,'placelist':placelist,'hoteldata':hoteldata})

def blog(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'blog.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'blog.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'blog.html')

def singleblog(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'blog-single.html',{'sessionuser':user,'name':data})
    # elif request.session.has_key('vendor'):
    #     vendor= request.session['vendor']
    #     data=VendorRegister.objects.get(vendoremail=vendor)
    #     return render (request,'blog-single.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'blog-single.html') 
    
def singlehotel(request,id):
    if request.session.has_key('user'):
        user = request.session['user']
        hoteldata = hotel.objects.get(id=id)
        return render(request,'singlehotel.html',{'sessionuser':user, 'hoteldata':hoteldata})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        hoteldata = hotel.objects.get(id=id)
        return render(request,'singlehotel.html',{ 'sessionvendor':vendor,'hoteldata':hoteldata})
    else:
        hoteldata = hotel.objects.get(id=id)
        return render(request,'singlehotel.html',{ 'hoteldata':hoteldata})

def userlogin(request):
    if request.POST:
        email = request.POST['email']
        pass1 = request.POST['pass']
        try:
            valid = UserRegister.objects.get(useremail=email,userpassword=pass1)
            if valid:
                request.session['user'] = valid.useremail
                request.session['username'] = valid.username
                request.session['usercontactno'] = valid.usercontactno
                request.session['user_address'] = valid.user_address
                request.session['userId'] = valid.pk
                print("Login sucesssss")
                return redirect('index')
            else:
                print("Login faiilllleedd")
                return render(request,'userlogin.html',{'messagekey':'Password incorrect'})
        except:
            return render(request,'userlogin.html',{'messagekey':'Password incorrect'})
    return render(request,'userlogin.html')

def vendorlogin(request):
    if request.POST:
        email = request.POST['email']
        pass1 = request.POST['pass']
        try:
            valid = VendorRegister.objects.get(vendoremail=email,vendorpassword=pass1)
            if valid:
                request.session['vendor'] = email
                request.session['vendorname'] = valid.vendorname
                request.session['vendorcontactno'] = valid.vendorcontactno
                request.session['vendor_address'] = valid.company_address
                request.session['vendorId'] = valid.pk
                return redirect('index')
            else:
                return render(request,'vendorlogin.html',{'messagekey':'Password incorrect'})
        except:
            return render(request,'vendorlogin.html',{'messagekey':'Password incorrect'})
    return render(request,'vendorlogin.html')

def userlogout(request):
    if 'user' in request.session.keys():
        del request.session['user']
        return redirect('index')
    return redirect('userlogin')

def vendorlogout(request):
    if 'vendor' in request.session.keys():
        del request.session['vendor']
        return redirect('index')
    return redirect('vendorlogin')

import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from datetime import date
def paymentofbooking(request): 
    if request.session.has_key('user'): 
        if request.method=="POST":        
            request.session['userid'] = request.session['userId']
            request.session['vendorid'] = request.POST['vendorid']
            request.session['hotelid'] = request.POST['hotelid']
            request.session['noofperson'] = request.POST['noofperson']
            request.session['user'] = request.session['user']
            data=VendorRegister.objects.get(id=request.session['vendorid'])
            request.session['Owner'] = data.vendorname
            request.session['hotel_name'] = request.POST['hotel_name']
            request.session['date1'] = request.POST['cheackin']
            request.session['date2'] = request.POST['cheackout']
            print(type(request.POST['cheackin']))
            a=request.POST['cheackin']
            b=request.POST['cheackout']
            data1=date(int(a[:4]),int(a[5:7]),int(a[8:]))
            data2=date(int(b[:4]),int(b[5:7]),int(b[8:]))
            data3=data2-data1
            data4 = data3.days
            print(type(data4))
            request.session['Amount'] = int(request.POST['Amount'])*int(data4+1)*int(request.POST['noofperson'])
            request.session['PaymentVia'] = "Online"
            request.session['PaymentMethod'] = "Razorpay"
            request.session['TransactionId'] = ""
            return redirect('razorpayView')  
    else:
        return redirect('userlogin')                

RAZOR_KEY_ID = 'rzp_test_8iwTTjUECLclBG'
RAZOR_KEY_SECRET = '0q8iXqBL1vonQGVQn4hK1tYg'
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

def razorpayView(request):
    currency = 'INR'
    amount = int(request.session['Amount'])*100
    # Create a Razorpay Order
    razorpay_order = client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'    
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpayDemo.html',context=context)

@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)
            
            amount = int(request.session['Amount'])*100  # Rs. 200
            # capture the payemt
            client.payment.capture(payment_id, amount)

            #Order Save Code
            orderModel = pymentdetails()
            orderModel.userid=request.session['userid']
            orderModel.vendorid=request.session['vendorid']
            orderModel.hotelid=request.session['hotelid']
            orderModel.noofperson=request.session['noofperson']
            orderModel.user = request.session['user']
            orderModel.Owner = request.session['Owner']
            orderModel.hotel_name = request.session['hotel_name']
            orderModel.PaymentVia = request.session['PaymentVia']
            orderModel.PaymentMethod = request.session['PaymentMethod']
            orderModel.Amount = request.session['Amount'] 
            orderModel.transactionId = payment_id
            orderModel.cheackin= request.session['date1'] 
            orderModel.cheackout= request.session['date2'] 
            orderModel.save()
            
            # render success page on successful caputre of payment
            return render(request,"suc.html")
        except:
            print("Hello")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("Hello1")
       # if other than POST request is made.
        return HttpResponseBadRequest()

def bookinghistory(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        data1=pymentdetails.objects.filter(userid=data.pk)
        return render (request,'bookinghistory.html',{'sessionuser':user,'name':data,'data':data1})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        data1=pymentdetails.objects.filter(vendorid=data.pk)
        return render (request,'bookinghistory.html',{'sessionvendor':vendor,'name':data,'data':data1})
    else:
        return render (request,'bookinghistory.html')