'''
Created on Oct 12, 2017

@author: Miguel
'''
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

app_name = settings.APP_NAME

urlpatterns = [
    url(r"^$", views.index),
    url(r"^index/$", views.index, name="index"),
    url(r"^registration/$", views.registration, name="registration"),
    url(r"^registration/confirmation/$", views.registration_cofirm, name="registration_confirm"),
    url(r"^activate_account/(?P<hashed_email>\w+@\w+\.\w+)/$", views.account_activation, name="activate_account"),
    # Esto esta causando error cundo trato de hacer un reverse
    #url(r"^login/$", auth_views.login, {"template_name", "photoadmin/site/login.html"}, name="login"),
    
]