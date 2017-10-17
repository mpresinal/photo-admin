'''
Created on Oct 15, 2017

@author: Miguel
'''
from django import forms
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.translation import ugettext

from . import models

COMMON_ATTRIB = {"class": "form-control"}

class RegistrationForm(forms.Form):
    
    name = forms.CharField(label=ugettext("Nombre"), max_length=60, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    last_name = forms.CharField(label=ugettext("Apellido"), max_length=60, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    email = forms.CharField(label=ugettext("Correo Electronico"), max_length=60, widget=forms.EmailInput(attrs=COMMON_ATTRIB))
    username = forms.CharField(label=ugettext("Usuario"), max_length=150, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    user_password = forms.CharField(label=ugettext(r"Contraseña"), max_length=10, widget=forms.PasswordInput(attrs=COMMON_ATTRIB))
    user_password_confirm = forms.CharField(label=ugettext(r"Repita la Contraseña"), max_length=10, widget=forms.PasswordInput(attrs=COMMON_ATTRIB))
    
    
    def process_form(self):
                        
        if self.is_valid():
            data = self.cleaned_data
            print(data)
            
            if data['user_password'] == data['user_password_confirm']:                
                
                new_user = User(first_name=data["name"], last_name=data["last_name"], username=data["username"])
                new_user.email=data["email"]
                new_user.set_password(data["user_password"])
                
                not_exist_user = self.validate_not_exist_user(self, new_user.username, new_user.email)
                
                if not_exist_user:
                    new_user.save()
                    return True                
                    
            else:
                print("password and confirmation password are not the same")
                self.add_error("user_password_confirm", ugettext(r"Las contraseñas no coinciden"))                 
        
        return False
            
    # End process_form method
    
    def validate_not_exist_user(self, user_name, user_email):
        """ 
        Validate a user does not exist with the specified username and email
        
        """    
        
        #
        # Checking if exists any user with the specified at user_name, if so
        # then add error to username field
        #
        try:            
            user = User.objects.get(username=user_name)          
            self.add_error("username", ugettext("Ya existe un usuario con este nombre"))
            
            return False
                                    
        except User.DoesNotExist:            
            pass
        
        #
        # Checking if exists any user with the specified user_email
        #
        try:
            user = User.objects.get(email=user_email)            
            self.add_error("email", ugettext("Ya existe un usuario con este nombre"))            
                
            return False
        
        except User.DoesNotExist:
            pass
        
        return True
    
    # end validate_not_exist_user
    
    def sent_confirmation_email(self, email):
        print("Sending email to: "+email)
        # Todo: pending to implement this method
        
    # end sent_confirmation_email
        
# end class
        