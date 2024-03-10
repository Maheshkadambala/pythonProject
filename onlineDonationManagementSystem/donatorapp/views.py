from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
def homepage(request):
    return render(request,'donatorhomepage.html')
def donateamt(request):
    return render(request,'donatorapp/donate.html')
def about(request):
    return render(request,'about.html')
