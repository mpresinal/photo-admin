from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import *
from . import forms
from django.contrib.auth import models as django_models;

# Create your views here.

APP_NAME = settings.APP_NAME

def index(request):
    return HttpResponseRedirect(reverse(APP_NAME+":registration"))
    #return render(request, "photoadmin/index.html", {}, "text/html");
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

def account_activation(request, hashed_email):
    ''' View function for activation account page
    '''
    form = None
    
    if request.method == "GET":
        
        initial_form_data = None
        
        # Todo: decode hashed_email to email address
        
        try:
            user = django_models.User.objects.get(email=hashed_email)        
    
            if user:
                # Initialize the dictionary
                initial_form_data = {
                    "name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email
                }
                
            # End if
        
        except(django_models.User.DoesNotExist):
            raise Http404("Does not exist user with this email: "+hashed_email)
        
        # End try-except
        
        form = forms.ActivationAccountForm(initial_form_data)
        
    else:
        form = forms.ActivationAccountForm(request.POST)
        
        # If everything was ok then redirect user to login page
        if form.process_form():
            return HttpResponseRedirect(reverse(APP_NAME+':login'));
            
    # End main if
    
    return render(request, "photoadmin/site/activate_account.html", {"app_name": APP_NAME, "form": form})

# End account_activation
        
