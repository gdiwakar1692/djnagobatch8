from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello Gaurav , i am on the earth!")

def about_page_view(request):  # new
    return render(request, "about.html")