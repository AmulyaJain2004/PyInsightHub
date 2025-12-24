from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignInForm
from .forms import SignUpForm
from .models import CustomUser
from .forms import ForgotPasswordForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            login(request, user)
            messages.success(request, 'Sign-up successful!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def signin_view(request):
    # Check if the request is a POST request (form submission)
    if request.method == 'POST':
        # Instantiate the form with POST data
        form = SignInForm(request.POST)
        # Validate the form
        if form.is_valid():
            # Extract cleaned data from the form
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authenticate the user with the provided email and password
            user = authenticate(request, email=email, password=password)
            # Check if authentication was successful
            if user is not None:
                # Log the user in
                login(request, user)
                # Display success message
                messages.success(request, 'Sign-in successful!')
                # Redirect to the home page or any other page
                return redirect('home')
            else:
                # Display error message if authentication failed
                messages.error(request, 'Invalid email or password.')
    else:
        # Instantiate an empty form if the request is not a POST request
        form = SignInForm()
    # Render the sign-in page with the form
    return render(request, 'signin.html', {'form': form})


def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Save method handles updating password and returning user object
            user = form.save()
            if user:
                # Log the user in after successful password reset
                login(request, user)
                messages.success(request, 'Password reset successful. You are now logged in.')
                return redirect('home')
            else:
                # Handle case where user does not exist (though form validation already checks this)
                messages.error(request, 'User does not exist.')
                return redirect('forgotpwd')
    else:
        form = ForgotPasswordForm()
    
    return render(request, 'forgotpwd.html', {'form': form})


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html', {'user':request.user})