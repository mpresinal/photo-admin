'''
Created on Oct 12, 2017

@author: Miguel
'''
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import site, portal

app_name = settings.APP_NAME

urlpatterns = [
    url(r"^$", site.index),
    url(r"^index/$", site.index, name="index"),
    url(r"^registration/$", site.registration, name="registration"),
    url(r"^registration/confirmation/$", site.registration_cofirm, name="registration_confirm"),
    url(r"^activate_account/(?P<hashed_email>\w+@\w+\.\w+)/$", site.account_activation, name="activate_account"),
    url(r"^activate_account/(?P<hashed_email>\w+@\w+\.\w+)/confirmation/$", site.account_activation_confirm,  name="activate_account_confirmation"),    
    url(r"^login/$", auth_views.login, name="login"),
    url(r"^portal/logout", auth_views.logout_then_login, name="logout"),
    url(r"^portal/$", portal.home),
    url(r"^portal/home/$", portal.home, name="home"),
    url(r"^portal/photoshoot/$", portal.photo_shoot_list, name="photoshoot"),
]