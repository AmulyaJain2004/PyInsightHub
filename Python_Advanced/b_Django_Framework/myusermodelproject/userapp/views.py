from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import UserRegistrationForm

# Create your views here.
def success(request):
    return render(request, 'success.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            
            user.save()
            return redirect('success')
        
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})
            
                 