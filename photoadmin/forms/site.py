'''
Created on Oct 15, 2017

@author: Miguel
'''
from django import forms
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.translation import ugettext
from django.db.models import ObjectDoesNotExist

from .. import models
from .. import utils

COMMON_ATTRIB = {"class": "form-control"}

LOGGER = utils.LoggerUtil()

class RegistrationForm(forms.Form):
    
    name = forms.CharField(label=ugettext("Nombre"), max_length=60, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    last_name = forms.CharField(label=ugettext("Apellido"), max_length=60, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    email = forms.CharField(label=ugettext("Correo Electronico"), max_length=60, widget=forms.EmailInput(attrs=COMMON_ATTRIB))
    username = forms.CharField(label=ugettext("Usuario"), max_length=150, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    user_password = forms.CharField(label=ugettext(r"Contrase{}a".format(u"\u00F1")), max_length=10, widget=forms.PasswordInput(attrs=COMMON_ATTRIB))
    user_password_confirm = forms.CharField(label=ugettext(r"Repita la Contrase{}a".format(u"\u00F1")), max_length=10, widget=forms.PasswordInput(attrs=COMMON_ATTRIB))
    
    
    def process_form(self):
                        
        if self.is_valid():
            data = self.cleaned_data
            print(data)
            
            if data['user_password'] == data['user_password_confirm']:                
                
                new_user = User(first_name=data["name"], last_name=data["last_name"], username=data["username"])
                new_user.email=data["email"]
                new_user.set_password(data["user_password"])
                new_user.is_active = False
                
                not_exist_user = self.validate_not_exist_user(new_user.username, new_user.email)
                
                print("not_exist_user = "+ str(not_exist_user))
                
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


class ActivationAccountForm(forms.Form):
    """ This class process the request of activation account form.
    """
    TEL_ATTRIB = {k:v for k,v in COMMON_ATTRIB.items()}
    TEL_ATTRIB['type'] = 'tel'
    
    FACEBOOK_URL = "https://www.facebook.com/"
    
    name = forms.CharField(label=ugettext("Nombre"), max_length=60, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    last_name = forms.CharField(label=ugettext("Apellido"), max_length=60, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    birthday = forms.DateField(label=ugettext("birthday"), required=False, widget=forms.DateInput())
    gender = forms.CharField(label=ugettext("Genero"), max_length=5, required=True, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    phone = forms.CharField(label=ugettext("Telefono"), max_length=30, required=False, widget=forms.TextInput(attrs=TEL_ATTRIB))
    cell_phone = forms.CharField(label=ugettext("Celular"), max_length=30, required=False, widget=forms.TextInput(attrs=TEL_ATTRIB))
    whatsapp = forms.CharField(label=ugettext("Whatsapp"), max_length=30, required=False, widget=forms.TextInput(attrs=TEL_ATTRIB))    
    email = forms.EmailField(label=ugettext("Email"), max_length=60, widget=forms.EmailInput(attrs=COMMON_ATTRIB))
    facebook = forms.CharField(label=ugettext("Whatsapp"), max_length=100, required=False, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    
    #Person Address fields
    
    address = forms.CharField(label=ugettext("Direcci&oacute;n"), max_length=220, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    city = forms.CharField(label=ugettext("Ciudad"), max_length=100, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    state = forms.CharField(label=ugettext("Estado")+'/'+ugettext("Provincia"), max_length=20, widget=forms.TextInput(attrs=COMMON_ATTRIB))    
    zip_code = forms.IntegerField(label=ugettext("C&oacute;digo Postal"), widget=forms.TextInput(attrs=COMMON_ATTRIB))
    country = forms.CharField(label=ugettext("Pa&iacute;s"), max_length=100, widget=forms.TextInput(attrs=COMMON_ATTRIB))
    
    # Contract Acceptance
    aggrement_acceptance = forms.BooleanField()
    
    def process_form(self):
        
        # Validating the form 
        if self.is_valid():
            form_data = self.cleaned_data;            
                
            person = self.get_person_instance(form_data)
            address = self.get_addres_instance(form_data)
            
            print("person = {}".format(person))
            print("address = {}".format(address))                      

            try:                           
                
                user = User.objects.get(email=person.email)
                print("user = {}".format(user))
                
                if not address.id:
                    # Saving address first
                    print("** Saving address...")
                    address.save();
                    print("address.id = {}".format(address.id))
                    print("** Saving address...DONE")
                    
                person.address = address
                
                # Saving person
                print("** Saving person...")
                person.user=user
                person.save()
                print("person.id = {}".format(person.id))
                print("** Saving person...DONE")
                
                # Activating account
                print("** Activating user accounts...")
                person.user.is_active = True                     
                person.user.save()                
                print("** Activating user accounts...DONE")                         

                return True
                                            
            except Exception as e:
                print("Error activating Account. {}".format(e))
                self.add_error(None, ugettext("Error activando cuenta"));
                
        else:
            print("Validation error. {}".format(self.errors))
                           
        return False                    
        
    # End process_form
    
    def activate_acount(self, user_email):
        
        # Getting user by email        
        try:
            user = User.objects.get(email=user_email)
            if user:
                if not user.is_active:
                    user.is_active = True;
                    user.save()
                    return user
                # End if
                
        except ObjectDoesNotExist:
            print("Error finding user by email")
            raise ObjectDoesNotExist()
            
        return None    
    #End activate_account
    
    def get_person_instance(self, data):
        '''
        return a Person instance using the fields related to a person.
        '''
        person = models.Person()
        person.name = data["name"]
        person.last_name = data["last_name"]
        person.birthday = data["birthday"]
        person.gender = data["gender"]
        person.phone = data["phone"]
        person.cell_phone = data["cell_phone"]
        person.email = data["email"]
        person.facebook = self.build_facebook_url()
        person.whatsapp = data["whatsapp"]
        
        return person              
        
    # End get_person_instance
    
    def get_addres_instance(self, data):
        '''
        return an Address instance using the fields related to an address.
        '''
        addr = models.Address()
        addr.address = data["address"].upper()
        addr.city = data["city"].upper()
        addr.state = data["state"].upper()
        addr.zip_code = data["zip_code"]
        addr.country = data["country"].upper()
        
        try:
            LOGGER.debug("Checking if already exist an address...")
            existing_address = models.Address.objects.get(address=addr.address, city=addr.city, 
                state=addr.state, zip_code = addr.zip_code, country=addr.country
            )
            
            if existing_address:
                LOGGER.debug("Address already exist!!")
                addr = existing_address
            
        except ObjectDoesNotExist as e:
            LOGGER.debug("Does not exist address with the information specified. {}".format(e))          

        return addr
    # End get_addres_instance
    
    def build_facebook_url(self):
        return ActivationAccountForm.FACEBOOK_URL + self.data["facebook"]
    
    # End method
    
    
# end calss





