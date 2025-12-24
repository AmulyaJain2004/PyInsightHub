from django.shortcuts import render, redirect
from .models import ContactModel
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():    
            # Form is valid, now create a Contact instance and save the data
            contact = ContactModel (
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                message = form.cleaned_data['message'])
            contact.save()
            # The reason we did not use form.save() is that form.save() is only available for ModelForm instances, not for Form instances. 
            # When you use forms.Form, it is not directly linked to a Django model, so there is no save() method provided. 
            # Instead, you have to manually handle the data and save it to the model yourself.
            # If you want to take advantage of the save() method, you should use forms.ModelForm which is designed to work directly with Django models.
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
            
def success(request):
    return render(request, 'success.html', context={'data':'success'})