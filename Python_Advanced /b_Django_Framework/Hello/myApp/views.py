from django.http import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is myApp index")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is myApp about")

def services(request):
    return HttpResponse("This is myApp services")

def contact(request):
    return HttpResponse("This is myApp contact")
