from django.shortcuts import render,redirect

# Create your views here.
from .models import BookModel
def book_page(request):

    if request.method=="POST":
        if request.user.is_authenticated:
            user = request.user  # Replace this with how you retrieve the email

            date = request.POST.get('date', '')
            timeslot = request.POST.get('timeslot', '')
            email = request.POST.get('email', '')
            
            # Assuming there's a model named BookModel defined in models.py
            book_model = BookModel(date=date, timeslot=timeslot, email=email)
            book_model.save()
        
        

        return redirect('dashboard_name')
    return render(request,'book.html')
