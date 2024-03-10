from django.shortcuts import render,HttpResponse ,redirect
from insti_app.views import MentorReg,InstiModel
from insti_app.models import PaymentModel,Mentee
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

    return render(request,'new.html')
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
