from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound,HttpResponseBadRequest
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import BookModel
import razorpay

from insti_app.models import PaymentModel
razorpay_client = razorpay.Client(auth=("rzp_live_WKs3ynkTOP8lcd", "fZeNBhZsubgV1SW3E4mD69kB"))
def book_page(request):

    if request.method=="POST":
        if request.user.is_authenticated:
            user = request.user  # Replace this with how you retrieve the email

            email=user.email

            date = request.POST.get('date', '')
            timeslot = request.POST.get('timeslot', '')
            email = request.POST.get('email', '')

            amount=100
            currency="INR"

            razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

            razorpay_order_id = razorpay_order['id']
            callback_url = 'paymenthandler/'
        
            # we need to pass these details to frontend.
            context = {}
            context['razorpay_order_id'] = razorpay_order_id
            context['razorpay_merchant_key'] = 'rzp_live_WKs3ynkTOP8lcd'
            context['razorpay_amount'] = amount
            context['currency'] = currency
            context['callback_url'] = callback_url
            return render(request, 'book_pay.html', context=context)
 
    return HttpResponseNotFound("<h1>Page not found</h1>")


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
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 100  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return redirect('dashboard_name')
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

           


# def book_page(request):

#     if request.method=="POST":
#         if request.user.is_authenticated:
#             user = request.user  # Replace this with how you retrieve the email

#             email=user.email

#             date = request.POST.get('date', '')
#             timeslot = request.POST.get('timeslot', '')
#             email = request.POST.get('email', '')



#             name=user.username
#             amount=100
        
#             client = razorpay.Client(auth=("rzp_live_WKs3ynkTOP8lcd", "fZeNBhZsubgV1SW3E4mD69kB"))

#             data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11","payment_capture":'1',"notes": {
#             "name": name,
#             "key2": "value2"
#         }}
#             payment = client.order.create(data=data)


#             print(payment)
#             PaymentModel(name=name,amount=amount,payment_id=payment['id']).save()
#             book_data={
#                 'date':date,'time_slot':timeslot,'email':email
#             }

        
            
#             # Assuming there's a model named BookModel defined in models.py
#             book_model = BookModel(date=date, timeslot=timeslot, email=email)
#             book_model.save()
#             return render(request,'book_pay.html',{'payment':payment,'book_data':book_data})
        
#         else: 

#             return redirect('dashboard_name')
#     return render(request,'book.html')


