from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RecordForm, SignUpForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect('home')
        else:
            messages.error(request, "Login Fail")
    return render(request, 'mysite/home.html', {'records': records})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "SignUp Successfully")
            return redirect('home')
    else: 
        form = SignUpForm()
    
    return render(request, 'mysite/register-form.html', {'form':form})


def record_detail(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(pk=pk);
        return render(request, 'mysite/record-detail.html', {'record': record})
    
    messages.success(request, 'Login first to view this page')
    return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        Record.objects.filter(pk=pk).delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')
    messages.success(request, "Record Deleted Fail...")
    return redirect('home')


def add_record(request):
    if request.user.is_authenticated:
        form = RecordForm(request.POST or None)
        if (request.method == 'POST'):
            if form.is_valid():
                form.save()
                messages.success(request, "Record has been added successfully")
                return redirect('home')
        return render(request, 'mysite/add_record.html', {'form':form})
    messages.success(request, "You Must Be Logged In...")
    return redirect('home') 


def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.filter(pk=pk).first()
        form = RecordForm(request.POST or None, instance=record)
        if (request.method == 'POST'):
            if form.is_valid():
                form.save()
                messages.success(request, "Record has been updated successfully")
                return redirect('home')
        return render(request, 'mysite/update_record.html', {'form':form})
    messages.success(request, "You Must Be Logged In...")
    return redirect('home')
            
            
	