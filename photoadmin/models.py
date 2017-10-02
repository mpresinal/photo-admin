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
    apartment = models.CharField(db_column="apartment", max_length=10, null=True, blank=True)
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
    address = models.ForeignKey(Address, db_column="address_id", on_delete=models.PROTECT)
    
    
    class Meta:
        db_table = "person"
        
# End Person class

class Photographer(CommonDateField):
    """ This class represents a photographer in the systen.
    
    """
    
    id = models.BigAutoField(db_column="photographer_id", primary_key=True)
    person = models.ForeignKey(Person, db_column="person_id", on_delete=models.CASCADE)
    
    # the water mark file name with extension
    water_mark_file = models.CharField(db_column="water_mark_file", max_length=50)
    
    class Meta:
        db_table="photographer"

# End Photographer class

class PhotoStudio(CommonDateField):
    """ This class represents a photo studio in the system.
    
    A photo studio is a place where a photographer works.
    """
    
    id = models.BigAutoField(db_column="photo_studio_id", primary_key=True)
    photographer = models.ForeignKey(Photographer, db_column="photographer_id", on_delete=models.CASCADE)
    name = models.CharField(db_column="name", max_length=100)
    street = models.CharField(db_column="street", max_length=200)    
    zip_code = models.CharField(db_column="zip_code", max_length=20)
    city = models.CharField(db_column="city", max_length=100)
    state = models.CharField(db_column="state", max_length=100)
    country = models.CharField(db_column="country", max_length=100)
    location = models.CharField(db_column="location", max_length=200)
    
    class Meta:
        db_table = "photo_studio"

# End PhotoStudio class


class PhotoPrinting(CommonDateField):
    """ This class represents a photo printing in the system.
    
    A photo printing is where a photographer goes to print their photos.
    """
    
    id = models.BigAutoField(db_column="photo_printing_id", primary_key=True)
    name = models.CharField(db_column="name", max_length=100)
    phone = models.CharField(db_column="phone", max_length=30)
    email = models.EmailField(db_column="email", max_length=100, null=False, blank=True)
    contact_name = models.CharField(db_column="contact_name", max_length=100)
    contact_phone = models.CharField(db_column="contact_phone", max_length=30)
    contact_email = models.EmailField(db_column="contact_email", max_length=100)
    address_street = models.CharField(db_column="street", max_length=200)    
    address_zip_code = models.CharField(db_column="zip_code", max_length=20)
    address_city = models.CharField(db_column="city", max_length=100)
    address_state = models.CharField(db_column="state", max_length=100)
    address_country = models.CharField(db_column="country", max_length=100)
    address_location = models.CharField(db_column="location", max_length=200, null=True, blank=False)
    photographers = models.ManyToManyField(
        Photographer,
        through="PhotographerPhotoPrinting",
        through_fields=("photoprinting","photographer")
    )
    
    class Meta:
        db_table = "photo_printing"
# End PhotoStudio class


class PhotographerPhotoPrinting(CommonDateField):
    """ This class is a mapping between Photographer and PhotoPrinting
    
    """
    
    # photographer_photoprinting will be an atribute in the class Photographer
    photographer = models.ForeignKey(
        Photographer,
        on_delete=models.CASCADE,
        db_column="photographer_id",
        related_name="photographer_photoprinting"
    )
    
    # photographer_photoprinting will be an atribute in the class PhotoPrinting
    photoprinting = models.ForeignKey(
        PhotoPrinting,
        on_delete=models.CASCADE,
        db_column="photo_printing_id",
        related_name="photographer_photoprinting"
    )
    
    
    # photo printing photographer code 
    photographer_code = models.CharField(db_column="photo_printing_code", max_length=10)
    
    class Meta:
        db_table="photographer_photo_printing"
    
# End class definition    


class PhotoShoot(CommonDateField):
    """ This class represents a photo shoot
    """
    id = models.BigAutoField(db_column="photo_shoot_id", primary_key=True)
    photographer = models.ForeignKey(
        Photographer,
        on_delete=models.CASCADE,
        db_column="photographer_id"        
    )
    
    name = models.CharField(db_column="name", max_length=100)
    description = models.CharField(db_column="description", max_length=256, null=True, blank=True)
    capture_time = models.DateTimeField(db_column="capture_time")
    
    class Meta:
        db_table="photo_shoot"

# End class PhotoShoot

class PhotoShootPhoto(CommonDateField):
    id = models.BigAutoField(db_column="photo_shoot_photo_id", primary_key=True)
    photo_file = models.ImageField(db_column="file")
    file_dir = models.CharField(db_column="directory", _max_length=200, null=False, blank=True)
    file_size = models.IntegerField(db_column="file_size", bull=False, blank=True)
    
    class Meta:
        db_table="photo_shoot_photo"

# End class PhotoShootPhoto




















