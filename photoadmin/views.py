from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, "photoadmin/index.html", {}, "text/html");
# End index function

def registration(request):
    return render(request, "photoadmin/site/register.html", {"app_name": settings.APP_NAME}, "text/html")    