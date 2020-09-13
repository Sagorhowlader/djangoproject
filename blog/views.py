from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def view_details():
    obj=Blogpost.objects.get(id=2)
    temp= "view_details.html"
    context = {"object": obj}
    return render(request,temp,context)