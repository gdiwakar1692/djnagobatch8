from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello, i am gaurav!")

def about_page_view(request):  # new
    return render(request, "about.html")