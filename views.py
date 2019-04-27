from django.http import HttpResponse
from django.shortcuts import render
from .forms import Help_and_SupportForm
from .formscust1 import Cust_SignupForm
from django.contrib.auth.views import  LoginView as auth_login
from django.contrib.auth import authenticate as auth
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  redirect
from django.contrib.auth.views import  LoginView as auth_login
from .models import Landdetails
from .formsld import LanddetailsForm
from .models import  Custdetails
from .formscd import CustdetailsForm


def base(request):
	return render(request,"base.html", {})
def about(request):
	return render(request,"about.html", {})
def logo(request):
	return render(request,"logo.html",{})
def logo1(request):
	return render(request,"logo1.html",{})
def q(request):
	return render(request,"q.html",{})
def mainpg(request):
	return render(request,"mainpg.html",{})
def backg1(request):
	return render(request,"backg1.html",{})
def home(request):
	return render(request,"home.html",{})
def backg2(request):
	return render(request,"backg2.html",{})
def cont(request):
	return render(request,"cont.html", {})
def how_it_works(request):
	return render(request,"how_it_works.html", {})
def help_and_support(request):

	if request.method == 'POST':
		form = Help_and_SupportForm(request.POST)
 
		if form.is_valid():
			form.save()
			return render(request, 'help_and_support.html')
	else:
		form = Help_and_SupportForm()
	return render(request, 'help_and_support.html', {'form': form})

def Cust_register(request):
	if request.method == 'POST':
		form = Cust_SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = auth(username=username, password=raw_password)
			
			form = CustdetailsForm()
			return render(request, 'Cdetails.html', {'form': form})

	else:
		form = Cust_SignupForm()
	return render(request, 'signup.html', {'form': form})

def Land_register(request):
	if request.method == 'POST':
		form = Cust_SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = auth(username=username, password=raw_password)
			
			form = LanddetailsForm()
			return render(request, 'Ldetails.html', {'form': form})
	else:
		form = Cust_SignupForm()
	return render(request, 'signupl.html', {'form': form})


def Cust_login(request):
	
	context = {}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth(request, username=username, password=password)
		if user:
			all_landd = Landdetails.objects.all()
			return render(request,"Maindisplay.html", {"all_landd" : all_landd})
		else:
			context['error'] = "provide valid crendetials"
			return render(request, "log.html", context)
	else:
		return render(request, "log.html", context)

def logout(request):
	return render(request, "logout.html", {})

def Ldetails(request):
	if request.method == 'POST':
		form = LanddetailsForm(request.POST)
 
		if form.is_valid():
			form.save()
			return render(request, 'own_message.html', {'form': form})
	else:
		form = LanddetailsForm()
	return render(request, 'Ldetails.html', {'form': form})

def Ldisplay(request):
	all_landd = Landdetails.objects.all()
	return render(request,"Ldisplay.html", {"all_landd" : all_landd})

def Cdetails(request):
	if request.method == 'POST':
		form = CustdetailsForm(request.POST)
 
		if form.is_valid():
			form.save()
			return render(request, 'log.html',  {'form': form})
	else:
		form = CustdetailsForm()
	return render(request, 'Cdetails.html', {'form': form})

def Maindisplay(request):
	all_landd = Landdetails.objects.all()
	return render(request,"Maindisplay.html", {"all_landd" : all_landd})



def payment(request):
	return render(request,"payment.html", {})

def forgot(request):
	return render(request,"forgot.html", {})

def Hostelselect(request):
	return render(request,"Hostelselect.html", {})

def own_message(request):
	return render(request,"own_message.html", {})














