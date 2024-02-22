from django.shortcuts import render,HttpResponse 

def home_page(request):

    return render(request,'index.html')



def demo_view(request):

    return render(request,'new.html')
