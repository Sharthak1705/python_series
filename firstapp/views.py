from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   return render(request, 'website/index.html')
   # return HttpResponse("Hello, world!. Welcome to my code in Home page")

def about(request):
    return render(request, 'website/about.html')
def contact(request):
    return HttpResponse("Hello, world!. Welcome to my code in Contact page")
def Run(request):
    return render(request, 'website/run.html')

