from django.db import models
from unittest.util import _MAX_LENGTH


class CommonDateField(models.Model):
    """This class provide the common date fields that every model must have.
    
    Those fields are:
    Creation Date: date time when it was created.
    Last update: date time of the last update
    
    """
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
# End CommonDateField class


class Address(CommonDateField):
    """ This class represents a person's address
    """
    id = models.BigAutoField(db_column="address_id", primary_key=True)
    street = models.CharField(db_column="street", max_length=200)
    appartment = models.CharField(db_column="appartment", max_length=10, null=True, blank=True)
    zip_code = models.CharField(db_column="zip_code", max_length=20)
    city = models.CharField(db_column="city", max_length=100)
    state = models.CharField(db_column="state", max_length=100)
    country = models.CharField(db_column="country", max_length=100)
    
    class Meta:
        db_table="address"
        
# End Address class
    
class Person(CommonDateField):
    """ This class represent a person in the system.
    
    """
    id = models.BigAutoField(db_column="person_id", primary_key=True)
    name = models.CharField(db_column="name", max_length=60)
    last_name = models.CharField(db_column="last_name", max_length=60)
    birthday = models.DateField(db_column="birthday", null=True, blank=True)
    phone = models.CharField(db_column="phone", max_length=30, null=True, blank=True)
    cell_phone = models.CharField(db_column="cell_phone", max_length=30)
    email = models.EmailField(db_column="email", max_length=100)
    facebook = models.CharField(db_column="facebook", max_length=100, null=True, blank=True)
    whatsapp = models.CharField(db_column="whatsapp", max_length=30, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    
    
    class Meta:
        db_table = "person"
        
# End Person class

class Photographer(CommonDateField):
    """ This class represents a photographer in the systen.
    
    """
    id = models.BigAutoField(db_column="photographer_id")
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    # the water mark file name with extension
    water_mark_file = models.CharField(db_column="water_mark_file", max_length=50)
    
    class Meta:
        db_table="photographer"

# End Photographer class
