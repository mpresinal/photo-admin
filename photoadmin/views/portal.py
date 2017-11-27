from django.shortcuts import render
from django.contrib.auth import decorators as django_decorators
from .common import *

from ..forms import portal as forms

@django_decorators.login_required        
def home(request):
    
    # get user from session
    user = request.user
    
    return render(request, "photoadmin/portal/home.html", create_context({"person": user.person}))

# End home view function

@django_decorators.login_required
def photo_shoot_list(request):
    
    form: forms.PhotoShootListForm = None
    context = create_context({"view_mode": "LIST"})
    
    if request.method == "POST":
        form = forms.PhotoShootListForm(request.POST)
        context['criteria'] = form.data['filter_criteria']
        
    else:
        form = forms.PhotoShootListForm()
    
    context["list"] = form.process_form();

    return render(request, "photoadmin/portal/photoshoot/photoshoot.html", context)
# end photo_shoot view function