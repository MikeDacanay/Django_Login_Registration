from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.messages import error
from models import *
# Create your views here.
def index(request):
	return render(request,"first/index.html")

def add(request):
    # errors = Users.objects.validate(request.POST)
    # if len(errors):
    #     for field, message in errors.iteritems():
    #         error(request, message, extra_tags=field)
    # 	return redirect('/')

	a = request.POST['First Name']
	b = request.POST['Last Name']
	c = request.POST['Email']
	d = request.POST['Confirm Password']
	Users.objects.create(first_name=a, last_name=b, email=c, password=d)
	
	return redirect('/success')

def success(request):
	return render(request,'first/success.html')