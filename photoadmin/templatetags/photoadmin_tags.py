from django import template

register = template.Library()

@register.simple_tag
def dict_value(dictionary, key, default_value=""):    
    
    value = ""
    
    if key in dictionary:
        value = dictionary[key]
        if not value:
            value = default_value
            
    return value

# End dict_value