from django.shortcuts import render,HttpResponse 
from insti_app.views import MentorReg,InstiModel
def home_page(request):

    return render(request,'index.html',{'insti_form':False,'menti_form':False,'contact_form':False,'dashboard':False })



def demo_view(request):

    return render(request,'new.html')

def dashboard_view(request):
    # Assuming you have retrieved the email from Google login
    if request.user.is_authenticated:
        user = request.user  # Replace this with how you retrieve the email
        user_email=user.email
        mentor_info = MentorReg.objects.filter(email=user_email).first()
        institute_info = InstiModel.objects.filter(email=user_email).first()

        context = {}
        context['user']=user
        
        context['mentor_info'] = mentor_info
        context['institute_info'] = institute_info
        if mentor_info:
            context['is_mentor'] = True
        elif institute_info:
            context['is_institute'] = True

        return render(request, 'dashboard.html', context)
    else:
        return render(request,'index.html',{'insti_form':False,'menti_form':False,'contact_form':False,'dashboard':True })
