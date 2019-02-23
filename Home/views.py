from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello")

def homePage(request):
    return render(request,'homebase.html')

def contact(request):
    return render(request,'contact.html')
