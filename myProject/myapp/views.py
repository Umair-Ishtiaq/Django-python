from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    context={
        "variable":"this is variable"
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, "Req sent.")
    return render(request,'contact.html')
