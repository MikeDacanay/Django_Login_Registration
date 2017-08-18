from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
import re
# import bcrypt
from models import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your views here.
def index(request):
	return render(request,"first/index.html")

def add(request):
	count=0
	if len(request.POST['name'])<4:
		messages.add_message(request,messages.INFO,'Name field is too short')
		count=1
	if len(request.POST['username'])<4:
		messages.add_message(request,messages.INFO,'UserName field is too short')
		count=1
	if request.POST["Password"]!=request.POST["Confirm Password"]:
		messages.add_message(request,messages.INFO,'password does not match')
		count=1
	if request.POST["Password"]<9:
		messages.add_message(request,messages.INFO,'password needs to be at least 8 characters long')
		count=1

	if count==1:
		return redirect('/')
	a = request.POST['name']
	b = request.POST['username']
	c = request.POST['datehired']
	d = request.POST['Confirm Password']
	Users.objects.create(name=a, username=b, datehired=c, password=d)
	request.session['id']=Users.objects.last().id
	print request.session['id']
	return redirect('/success')

def login(request):
	user_db=Users.objects.all()
	for user in user_db:
		if user.username==request.POST['username']:
			if user.password==request.POST['pass_log']:
				request.session['id']=Users.objects.get(username=request.POST['username']).id
				return redirect('/success')
	messages.add_message(request,messages.INFO,'invalid login information')
	return redirect('/')

def success(request):
	request.session['name']=Users.objects.get(id=request.session['id']).name
	wished_db= Users.objects.get(id=request.session['id']).items.all()
	all_wish_db= Items.objects.exclude(creator_id=request.session['id'])
	context ={
		'wish_pane': wished_db,
		'all_pane':all_wish_db,
		'wisher': request.session['id']
	}
	print wished_db
	return render(request,'first/success.html',context)
def delete(request, idx):
	b=Items.objects.get(id=idx)
	b.delete()
	return redirect('/success')

def create(request):
	return render(request,'first/create_item.html')

def add_item(request):
	print request.POST['item']
	b=Items.objects.create(Item=request.POST['item'], creator=Users.objects.get(id=request.session['id']))
	user=Users.objects.get(id=request.session['id'])
	b.users.add(user)
	b.save()
	return redirect('/success')

def take_wish(request, idx):
	u=Users.objects.get(id=request.session['id'])
	b=Items.objects.get(id=idx)
	b.users.add(u)
	return redirect('/success')

def remove_wish(request, idx):
	b=Items.objects.get(id=idx)
	u1=Users.objects.get(id=request.session['id'])
	b.users.remove(u1)
	b.save()
	return redirect('/success')

def check(request, idx):
	z=Items.objects.get(id=idx)
	y=Items.objects.get(id=idx).users.all()
	checker= {
		"item":z,
		"userz":y
	}
	return render(request,'first/check.html',checker)

def logout(request):
	del request.session['id']
	return redirect('/')

