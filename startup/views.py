from django.shortcuts import render,HttpResponse ,redirect
from insti_app.views import MentorReg,InstiModel
from insti_app.models import PaymentModel,Mentee
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def home_page(request):

    return render(request,'index.html',{'insti_form':False,'menti_form':False,'contact_form':False,'dashboard':False })
import razorpay


#payment section
def payment_view(request):
    if request.method =='POST':
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))*100
    
        client = razorpay.Client(auth=("rzp_live_WKs3ynkTOP8lcd", "fZeNBhZsubgV1SW3E4mD69kB"))

        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11","payment_capture":'1',"notes": {
        "name": name,
        "key2": "value2"
    }}
        payment = client.order.create(data=data)
        print(payment)
        PaymentModel(name=name,amount=amount,payment_id=payment['id']).save()

        return render(request,'payment.html',{'payment':payment})
    return render(request,'payment.html')
def success_view(request):
    return render (request,'success.html')



def demo_view(request):

    return render(request,'demo.html')
def privacy_view(request):
    return render(request,'privacy.html')

def terms_view(request):
    return render(request,'terms.html')

from book.models import BookModel
def dashboard_view(request):
    # Assuming you have retrieved the email from Google login
    if request.user.is_authenticated:
        user = request.user  # Replace this with how you retrieve the email
        user_email=user.email
        mentor_info = MentorReg.objects.filter(email=user_email).first()
        institute_info = InstiModel.objects.filter(email=user_email).first()

        mentee_info=Mentee.objects.filter(email=user_email).first()

        appointments = BookModel.objects.filter(email=user_email)
        context = {}
        context['appointments']=appointments
        context['mentee_update']= True
        if mentee_info:
            context['mentee_update']=False 
        

        context['user']=user
        
        context['mentor_info'] = mentor_info
        context['mentee_info'] = mentee_info
        context['institute_info'] = institute_info
        if mentor_info:
            context['is_mentor'] = True
        elif institute_info:
            context['is_institute'] = True

        return render(request, 'dashboard.html', context)
    else:
        return render(request,'index.html',{'insti_form':False,'menti_form':False,'contact_form':False,'dashboard':True })



from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound,HttpResponseBadRequest
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from book.models import BookModel
import razorpay

from insti_app.models import PaymentModel
razorpay_client = razorpay.Client(auth=("rzp_live_WKs3ynkTOP8lcd", "fZeNBhZsubgV1SW3E4mD69kB"))
def book_appoint(request):

    if request.method=="POST":
        if request.user.is_authenticated:
            user = request.user  

            email=user.email

            date = request.POST.get('date', '')
            timeslot = request.POST.get('timeslot', '')
            email = request.POST.get('email', '')

            

            amount=500
            currency="INR"

            razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

            razorpay_order_id = razorpay_order['id']

            book_model = BookModel(date=date, timeslot=timeslot, email=email,order_id=razorpay_order_id)
            book_model.save()
            callback_url = 'bookpayment'
        
            # we need to pass these details to frontend.
            context = {}
            context['razorpay_order_id'] = razorpay_order_id
            context['razorpay_merchant_key'] = 'rzp_live_WKs3ynkTOP8lcd'
            context['razorpay_amount'] = amount
            context['currency'] = currency
            context['callback_url'] = callback_url
            return render(request, 'gfg_index.html', context=context)
    
    return render(request,'book.html')

def order_payment(request):

    if request.method=="POST":
        if request.user.is_authenticated:
            user = request.user  

            email=user.email

            

            amount=100
            currency="INR"


            razorpay_order_id = request.POST.get('order_id')

            # book_model = BookModel(date=date, timeslot=timeslot, email=email,order_id=razorpay_order_id)
            # book_model.save()
            callback_url = 'bookpayment'
        
            # we need to pass these details to frontend.
            context = {}
            context['razorpay_order_id'] = razorpay_order_id
            context['razorpay_merchant_key'] = 'rzp_live_WKs3ynkTOP8lcd'
            context['razorpay_amount'] = amount
            context['currency'] = currency
            context['callback_url'] = callback_url
            return render(request, 'gfg_index.html', context=context)
    
    return render(request,'book.html')


@csrf_exempt
def paymentbook(request):
 
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
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 100  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    book_obj=BookModel.objects.get(order_id=razorpay_order_id)

    # Update the completed field to True
                    book_obj.completed = True
                    book_obj.save()
                    # render success page on successful caputre of payment
                    return render(request,'success.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'fail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'fail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
    



def logout_view(request):
    
    logout(request)
    messages.success(request,'Logout successful')
    return redirect('/')

 
def login_view(request):
    if request.method=='POST':
        user_onsite=request.POST.get("uname")
        passw=request.POST.get("pass1")


        if authenticate(username=user_onsite,password=passw) is not None:
            login(request,authenticate(username=user_onsite,password=passw))
            messages.success(request,'Login successful')
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')

    return render(request,'login.html')
def signup_view(request):
    if request.method=='POST':
        uname1=request.POST.get("uname")
        email1=request.POST.get("email")
        password=request.POST.get("pass1")
        re_pass=request.POST.get("pass2")
        # print(username,email,password,re_pass)
        try:
            if User.objects.get(username=uname1):
                    messages.warning(request,'username is already taken')
                    return redirect('/signup')
        except:
            pass
        
        try:
            if User.objects.get(email=email1):
                    messages.info(request,'This email is already registered')
                    return redirect('/signup')
        except: 
            pass
        
        try:
            if password!=re_pass:
                    messages.warning(request,'password mismatch')
                    return redirect('/signup')
        except:
            pass
        user=User.objects.create_user(uname1,email1,password)
        user.save()
        messages.success(request,'Sign Up Successfully')
        return redirect('/login')
    return render(request,'signup.html')


           