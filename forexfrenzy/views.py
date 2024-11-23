

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'forexfrenzy/about.html')

def contact(request):
    return render(request, 'forexfrenzy/contact.html')