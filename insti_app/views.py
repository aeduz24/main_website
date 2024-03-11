from django.shortcuts import render,HttpResponse,redirect
from .models import InstiModel,ContactModel,MentorReg
# Create your views here.



def insti_page(request):

    return render(request,'institute.html')



def submitted_insti(request):
    if request.method == "POST":
        name = request.POST.get('insti_name', '')
        email = request.POST.get('insti_email', '')
        mobileNo = request.POST.get('insti_tel', '')
        website = request.POST.get('insti_web', '')
        address = request.POST.get('insti_loc', '')
        colgStu = request.POST.get('insti_stu', '')
        exam = request.POST.get('insti_exam', '')
        feedback = request.POST.get('insti_text', '')

        # Assuming there's a model named InstiModel defined in models.py
        response = InstiModel(name=name, email=email, mobileNo=mobileNo,website=website,
                              address=address, colgStu=colgStu, exam=exam, feedback=feedback)
        response.save()

        return  render(request,'index.html',{'insti_form':True,'menti_form':False,'contact_form':False,'dashboard':False })
    else:
        return  render(request,'index.html',{'insti_form':False,'menti_form':False,'contact_form':False,'dashboard':False })

    return HttpResponse('Invalid method')  # Handling other HTTP methods
def submit_view(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        mobileNo = request.POST.get('tel', '')
        
        message = request.POST.get('message', '')

        # Assuming there's a model named InstiModel defined in models.py
        response = ContactModel(name=name, email=email, mobileNo=mobileNo,message=message)
        response.save()

        return render(request,'index.html',{'insti_form':False,'menti_form':False,'contact_form':True,'dashboard':False })

    return  render(request,'index.html',{'insti_form':False,'menti_form':False,'contact_form':False,'dashboard':False })  # Handling other HTTP methods

from .models import Mentee

def mentee_reg_view(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        college = request.POST.get('coaching', '')
        year_of_study=request.POST.get('yearOfStudy','')
        # Check if a Mentee object with the same email exists
        existing_mentee = Mentee.objects.filter(email=email).first()

        if existing_mentee:
            # Delete the existing object
            existing_mentee.delete()

        # Save the new Mentee object
        mentee_registration = Mentee(name=name, email=email, contact=contact, coaching=college,year_of_study=year_of_study)
        mentee_registration.save()

    return redirect('dashboard_name')


def mentor_reg_view(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        coaching = request.POST.get('coaching', '')
        year_of_study=request.POST.get('yearOfStudy','')
      
        
        # Assuming there's a model named MentorRegistration defined in models.py
        mentor_registration = MentorReg(name=name, email=email, contact=contact, coaching=coaching, year_of_study=year_of_study)
        mentor_registration.save()

        return render(request,'index.html',{'insti_form':False,'menti_form':True,'contact_form':False,'dashboard':True })
    else:
        return  render(request,'index.html',{'insti_form':False,'menti_form':False,'contact_form':False,'dashboard':False })
    




 
