'''
Created on Nov 26, 2017

@author: Miguel
'''

from django import forms
from .. import models

class PhotoShootListForm(forms.Form):
    
    filter_criteria = forms.CharField(max_length=100, required=False)
    
    def process_form(self):
        """ This method process the action of Management Photo Shoot page
        """
        
        # Process filter
        criteria = None
        if 'filter_criteria' in self.data:
            criteria = self.data['filter_criteria']
            
        # End if
        
        querySet = None
         
        if criteria:
            querySet = models.PhotoShoot.filter_by_name_or_description(criteria)
            
        else:
            querySet = models.PhotoShoot.objects.filter()
            
        return querySet

    # End method

# End class

class PhotoShootForm(forms.Form):
    
    
    
    def process_list_form(self):        
        pass
    
    pass
# End class
