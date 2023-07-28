from django.forms import ModelForm
from user.models import CustomUser

class CustomUserCreationForm(ModelForm):

    class Meta:

        #in model form , specify the fields to use
        model = CustomUser
        fields = ['username','password','phone','email']

