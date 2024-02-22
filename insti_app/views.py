from django.shortcuts import render,HttpResponse
from .models import InstiModel
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

        return HttpResponse('Form is successfully submitted')

    return HttpResponse('Invalid method')  # Handling other HTTP methods
