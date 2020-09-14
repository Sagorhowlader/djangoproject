from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django import forms
from .form import ContactForm
def home_page(request):
        mytitle = "Homepage"
        context = {"title": mytitle,"Body":"HomePage"}
        return render(request,"home.html",context)



def about(request):
                return render(request,"about.html",{"title":"About us","Body":"About Us Page"})

def contact(request):
                form = ContactForm(request.POST or None)
                if form.is_valid():

                    print(form.cleaned_data)
                    form = ContactForm()
                context = {"title":"contact",
                           "Body":"Contact Page",
                           "form": form
                }
                return render(request,"form.html",context)