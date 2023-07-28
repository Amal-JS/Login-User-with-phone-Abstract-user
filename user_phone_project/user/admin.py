from django.contrib import admin
from .models import CustomUser


#register the custom user model
admin.site.register(CustomUser)