from urllib import request

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout     
from django.contrib import messages
from .models import Record

from website.models import Record
from .forms import SignUpForm
# Create your views here.

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in. Please try again.")
            return redirect('home')
    else:   
        return render(request,'home.html',{'records': records})



def add_record(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']

        new_record = Record.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code
        )
        new_record.save()
        messages.success(request, "Record has been added.")
        return redirect('home')
    return render(request, 'add_record.html')

def logout_user(request):

     logout(request)
     messages.success(request, "You have been logged out.")
     return redirect('home')

def customer_record(request, pk):
    customer_record = Record.objects.get(id=pk)
    return render(request, 'record.html', {
        'customer_record': customer_record
    })
def update_record(request, pk):
    current_record = Record.objects.get(id=pk)

    if request.method == 'POST':
        current_record.first_name = request.POST['first_name']
        current_record.last_name = request.POST['last_name']
        current_record.email = request.POST['email']
        current_record.phone_number = request.POST['phone_number']
        current_record.address = request.POST['address']
        current_record.city = request.POST['city']
        current_record.state = request.POST['state']
        current_record.zip_code = request.POST['zip_code']

        current_record.save()

        messages.success(request, "Record Updated")
        return redirect('home')

    return render(request, 'update_record.html', {
        'current_record': current_record
    })

from django.shortcuts import redirect

def delete_record(request, pk):
    
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Record has been deleted.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})