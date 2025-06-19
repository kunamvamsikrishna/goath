from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import logout 

# Create your views here.
def login(request):
    if request.method == "POST":
         name = request.POST.get("username")    
         password = request.POST.get("password")
         User.objects.create_user(username=name,password=password)
         return redirect('profile')
    return render (request,'login.html')

def home(request):
    all_users = User.objects.all()
    return render(request, 'home.html', {'users': all_users})

def logoutt(requset):
    logout(requset)
    return redirect('login')

def profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request,'profile.html',{"user":user})
