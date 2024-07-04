from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

  
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have login succesfully!")
            return redirect('home')
        else:
            messages.success(request,"we couldn't find an account with that username.Try another")
            return redirect('home')
    else:
        return render(request,'home.html') 
     
    return render(request,'home.html') 
      
