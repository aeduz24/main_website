from django.shortcuts import render,redirect

# Create your views here.
from .models import BookModel
import razorpay

from insti_app.models import PaymentModel

def book_page(request):

    if request.method=="POST":
        if request.user.is_authenticated:
            user = request.user  # Replace this with how you retrieve the email

            email=user.email

            date = request.POST.get('date', '')
            timeslot = request.POST.get('timeslot', '')
            email = request.POST.get('email', '')



            name=user.username
            amount=100
        
            client = razorpay.Client(auth=("rzp_live_WKs3ynkTOP8lcd", "fZeNBhZsubgV1SW3E4mD69kB"))

            data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11","payment_capture":'1',"notes": {
            "name": name,
            "key2": "value2"
        }}
            payment = client.order.create(data=data)


            print(payment)
            PaymentModel(name=name,amount=amount,payment_id=payment['id']).save()
            book_data={
                'date':date,'time_slot':timeslot,'email':email
            }

        
            
            # Assuming there's a model named BookModel defined in models.py
            book_model = BookModel(date=date, timeslot=timeslot, email=email)
            book_model.save()
            return render(request,'book_pay.html',{'payment':payment,'book_data':book_data})
        
        else: 

            return redirect('dashboard_name')
    return render(request,'book.html')


