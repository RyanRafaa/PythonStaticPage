from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def screenOne(request):
    return render(request, 'screenOne.html')

def screenTwo(request):
    return render(request, 'screenTwo.html')