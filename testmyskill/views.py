from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
def home_page(request):
        mytitle = "Hello"
        context = {"title": mytitle}
        return render(request,"home.html",context)



def about(request):
                return render(request,"about.html",{"title":"about us"})

def contact(request):
                return render(request,"contact.html",{"title":"contact"})