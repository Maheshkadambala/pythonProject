from django.shortcuts import render,redirect

from .models import charityDetails2


# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
def homepage(request):
    return render(request,'generalhomepage.html')
def charitypost(request):
    return render(request,'generalapp/charity.html')

def add_charity_details(request):
    if request.method=='POST':

        org_name=request.POST.get('org_name')
        purpose=request.POST.get('purpose')
        location=request.POST.get('location')



        charity_details=charityDetails2(
            org_name=org_name,
            purpose=purpose,
            location=location,


        )
        charity_details.save()
        return render(request,'generalapp/datainserted.html')
    return render(request,'generalapp/charity.html')

def view_charity_detail(request):
    charity_details_list=charityDetails2.objects.all()
    return render(request,'generalapp/viewCharityDetails.html', {'view_charity_detail':charity_details_list})

def about(request):
    return render(request,'about.html')


def deletecharity(request,pk):
    return HttpResponse("<h1>Data deleted successfully</h1>")
    # charityDetails2.objects.filter(id=id).delete()
    #
    # return HttpResponse("<h1>deleted</h1>")


