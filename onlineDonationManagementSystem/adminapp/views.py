from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


from django.contrib.auth.models import User




# Create your views here.
def projecthomepage(request):
    return render(request,'projecthomepage.html')


def donatorhomepage(request):
    return render(request,'donatorhomepage.html')

def generalhomepage(request):
    return render(request,'generalhomepage.html')
def signup(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, "Password does not match")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name, last_name=last_name)
        user.save()
        return redirect('login')

    return render(request,'signup.html')




def login(request):
    if request.method == "POST":
        username1 = request.POST["uname"]
        password = request.POST["pwd"]
        x=auth.authenticate(username=username1,password=password)
        if x is None:
            return HttpResponse("<h1>USER NOT AVAILABLE</h1>")
            return redirect('login')

        else:
            return render(request, 'donatorapp/donate.html')

    return render(request, 'login.html')

    # if request.method == "POST":
    #     username1 = request.POST["uname"]
    #     password = request.POST["pwd"]
    #     if username1 == "uday" and password == "123":
    #         return render(request, 'donatorapp/donate.html')
    #     else:
    #         return render(request, 'login.html')
    # return render(request, 'login.html')






def about(request):
    return render(request,'about.html')

def successpage(request):
    if request.method=='POST':
        amount=request.POST['amt']
        user=request.POST['uname']
        return HttpResponse("<h1>thank you donating</h1>")
    return render(request,'donatorapp/successpage.html')

def linked(request):
    return render(request,'donatorapp/linked.html')

def phone(request):
    return render(request,'donatorapp/phone.html')

def insta(request):
    return render(request,'donatorapp/insta.html')





