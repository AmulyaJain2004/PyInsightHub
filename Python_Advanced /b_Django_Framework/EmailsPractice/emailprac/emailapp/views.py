from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from emailapp.forms import UserRegistrationForm

def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    email_from = 'jainamulyawin@gmail.com'
    recipient_list = ['amulyajain180489@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse('Email sent successfully!')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            
            user.save()
            return redirect('send_email')
        
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})
            