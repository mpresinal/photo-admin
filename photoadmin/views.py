from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import forms

# Create your views here.

APP_NAME = settings.APP_NAME

def index(request):
    return render(request, "photoadmin/index.html", {}, "text/html");
# End index function

def registration(request):
    form = None
    
    if request.method == "POST":
        # process request
        form = forms.RegistrationForm(request.POST)
        
        #validate the form
        sucess = form.process_form() # bool(request.POST['agree_terms'])
        
        if sucess:
            return HttpResponseRedirect(reverse(APP_NAME+":registration_confirm"))
            
    else:
        form = forms.RegistrationForm()
        
    return render(request, "photoadmin/site/register.html", {"app_name": APP_NAME, "form": form}, "text/html")
# End registration view

def registration_cofirm(request):
    return render(request, "photoadmin/site/register_cofirm.html", {"app_name": APP_NAME})    