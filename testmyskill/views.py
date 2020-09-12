from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
        mytile="home"
        return render(request,"home.html",{"title":mytile})

