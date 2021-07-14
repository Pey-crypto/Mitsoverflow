from django.shortcuts import render,redirect
from .forms import UserRegisteration
from django.contrib.auth import authenticate,login,logout
from forum.models import * 
from django.contrib import messages
# Create your views here.
def home(request):
    try:
        item = forum.objects.all()
    except:
        item = None
    return render(request,"index.html",{'item':item})

def userregistration(request):
    form = UserRegisteration()
    if request.method == 'POST':
        form = UserRegisteration(request.POST)
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request,username+'your account is created')
            return redirect('login')
    context={'form':form}
    return render(request,'register.html',context)

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('forum:home')
        else:
            messages.info(request,"Invalid")

    return render(request,'login.html')

def userlogout(request):
    logout(request)
    try:
        item = forum.objects.all()
    except:
        item = None
    return render(request,"index.html",{'item':item})
