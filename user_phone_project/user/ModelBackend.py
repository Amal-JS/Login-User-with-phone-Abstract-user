from django.contrib.auth.backends import ModelBackend

#used to get the current user model in the project
from django.contrib.auth import get_user_model

#if the object doesn't exist using this objectdoesnotexist exception we can catch this
from django.core.exceptions import ObjectDoesNotExist


'''

from this ModelBackend if user exists we get the user instance back to the views else
we wil get 'None'

'''



class MultiFieldAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        
        UserModel = get_user_model()
        # Check if the provided username is a valid email
        try:
                user = UserModel.objects.get(email=username)
                
        #Checking the password of the user if a 'user' exists with that email

                if user.check_password(password):
                    #if password also same then return user
                    return user
        except ObjectDoesNotExist:
            # If not found by email, check if it's a valid username
            try:
                
                    user = UserModel.objects.get(username=username)
                    
                    if user.check_password(password):
                        return user
                    
            except ObjectDoesNotExist:

                # If not found by username or email, try with the provided phone as-is
                try:
                    user = UserModel.objects.get(phone=username)
                
                    if user.check_password(password):
                            return user
                except ObjectDoesNotExist:
                     return None
                
            
        
