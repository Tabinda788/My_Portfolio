from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    context = {"name": 'Tabinda', 'course': 'Data Science'}
    return render(request,'home.html', context)


def about(request):
    # return HttpResponse("This is my aboutpage (/about)")
    return render(request,'about.html')

def project(request):
    # return HttpResponse("This is my projectpage (/project)")
    return render(request,'projects.html')
  
def experience(request):
    return render(request, "experience.html")

def contact(request):
    # return HttpResponse("This is my contactpage (/contact)")
    if request.method=="POST":   
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name,email,phone,desc)
        contact = Contact(name=name, email=email,phone=phone, desc=desc)
        contact.save()
        print("The data has been saved to the db")

    return render(request,'contact.html')

