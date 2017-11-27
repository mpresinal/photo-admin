'''
Created on Nov 26, 2017

@author: Miguel Presinal
'''

from django.conf import settings
from datetime import date

# Create your views here.

APP_NAME = settings.APP_NAME

APP_COPY_RIGHT = {'app_name': settings.APP_DISPLAY_NAME, 'year': date.today().year}

# Default context used by all view's template file
DEFAULT_CONTEXT = {"app_name": APP_NAME, "copy_right": APP_COPY_RIGHT, "context_path": "photoadmin", "form": None}


def create_context(initial_context: dict = None):
    ''' 
    This function create a tamplate context using DEFAULT_CONTEXT.
    This function merge the dict passed as argument with DEFAULT_CONTEXT and return a new dict
    
    '''
    context = {k:v for k,v in DEFAULT_CONTEXT.items()}
    
    if initial_context:
        for k,v in initial_context.items():
            context[k] = v;
    
    return context

# End create_context function