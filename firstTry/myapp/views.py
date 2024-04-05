from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
	return render(request, "index.html")

def login(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
			
		user = auth.authenticate(username = username, password = password)
			
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			return redirect('login')
	else:
		return render(request, "login.html")
	
def register(request):
		if request.method == "POST":
			username = request.POST["username"]
			password = request.POST["password"]
		
			user = User.objects.create_user(username = username, password = password);
			user.save();
		
			return redirect("login")
		else:
			return render(request, "register.html")

def logout(request):
	auth.logout(request)
	return redirect("/")
	
