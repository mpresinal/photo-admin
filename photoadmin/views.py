from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.http import *
from django.contrib.auth import models as django_models

from . import forms
from . import models
from django.contrib.postgres.aggregates import general

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
    data_context = {"app_name": APP_NAME}
    data_context["start_at_step"] = 0  
    
    wizard_step_one_failed = False
    wizard_step_two_failed = False
    wizard_step_three_failed = False
    
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
            return HttpResponseRedirect(reverse(APP_NAME+':activate_account_confirmation', args=(hashed_email,)));
        
        else:
            data_context["gender"] = form.data['gender']
            data_context["country"] = form.data['country']
            
            # if some error occurre while procesing the form then display errors to user            
            general_errors = form.non_field_errors()
            print(general_errors)
            
            if general_errors:
                data_context["error"] = general[0]
                
            else:                                
                data_context["validation_fail"] = True
                                
                # add to data_context failed fields dict
                for key in form.errors.keys():
                    
                    # Determing which wizard step must be displayed based
                    # on failed fields validation
                    if not wizard_step_one_failed and key in ("name", "last_name", "birthday", "email"):
                        wizard_step_one_failed = True    
                        
                    elif not wizard_step_two_failed and key in ("address", "city", "state", "zip_code", "country"):
                        wizard_step_two_failed = True  
                        
                    elif not wizard_step_three_failed and key == "aggrement_acceptance":
                        wizard_step_three_failed = True
                        
                    data_context[key+"_valid"] = False

            print("wizard_step_one_failed = ", wizard_step_one_failed)
            print("wizard_step_two_failed = ", wizard_step_two_failed)
            print("wizard_step_three_failed = ", wizard_step_three_failed)
               
            if wizard_step_two_failed and not wizard_step_one_failed:
                data_context["start_at_step"] = 1
                
            elif wizard_step_three_failed and not wizard_step_two_failed:
                data_context["start_at_step"] = 2
                                 
                           
        # End proces_form if-else   
            
            
    # End main if  
    
    data_context["form"] = form    
    
    print(data_context)
    
    return render(request, "photoadmin/site/activate_account.html", data_context)

# End account_activation

def account_activation_confirm(request, hashed_email):
    print("account_activation_confirm() Enter");
    person = get_object_or_404(models.Person, email=hashed_email)
    return render(request, "photoadmin/site/activate_account_confirm.html", {"app_name": APP_NAME, "name": person.name, "last_name": person.last_name, "gender": person.gender })
    
# End account_activation_confirm function
        
