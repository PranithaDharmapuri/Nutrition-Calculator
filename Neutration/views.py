from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FoodItem
def home(request):
    return render(request,'home.html')
def admin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('home')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'user.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def register(request):
    if request.method =='POST':
        First_Name = request.POST['name']
        Email=request.POST['email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['cnfm_password']
        select_user=request.POST['select_user']
        if select_user == 'admin':
            select_user=True
        else :
            select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'register.html')
def dashboard_view(request):
    
    return render(request,'nutrition.html',)
def udashboard_view(request):  
    data= FoodItem.objects.all()
    if request.method=="POST":
        pk=request.POST['receipe']
        Quantity=request.POST['servings']
        quantity=int(Quantity)
        item=FoodItem.objects.get(id=pk)
        return render(request,'Unutrional.html',
                      {
                        'fooditems':data,
                        'item':item,
                        'calaries':item.calaries*quantity,
                        'protien':item.protien*quantity,
                        'fat':item.fat*quantity,
                        'carbohydrates':item.carbohydrates*quantity,
                        })
    return render(request,'Unutrional.html',{'fooditems':data})