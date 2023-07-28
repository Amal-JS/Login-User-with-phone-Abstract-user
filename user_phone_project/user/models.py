from django.db import models

# importing AbstractUser model from django.contrib.auth.models

from django.contrib.auth.models import AbstractUser

#checking min length

from django.forms import ValidationError

# Create your models here.


class CustomUser(AbstractUser):


    def min_length(value):
            if len(value)< 10 or len(value)>10:
                raise ValidationError("Phone number want to be 10 digit")

    phone = models.CharField(max_length=10,blank=False,null=False,validators=[min_length])




    '''
    By default blank and null for a model field is True .

    so here i have added the constraint blank = false and null = false

    ? blank = false  

        blank is used for a form validation purpose.So when we are creating or updating
        an existing object this phone field must have a value .If it's empty then a 
        we will get a form validation error stating that this is a required field.

    ? null =  false

        here null is related to the  database representation of that field so, by default
        it is True .So if we did'nt provide a value it will set null for that particular 
        field in the database.
        Now null = false says You want to have a value when submiting a new record.
        Empty is not permitted
    
    '''

    

    def __str__(self):
        return self.username
    
    
    

''' 
After this now we have to set in settings that our CustomUser want to be used as
the User model in our django project . So now go to settings.py and add
AUTH_USER_MODEL = 'user.CustomUser'

'''