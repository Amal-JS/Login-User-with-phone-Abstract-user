from django.urls import path
from . import views

urlpatterns=[

path("",views.index,name="index"),
#path for creating a new user account
path("create_account/",views.create_user,name="create"),
#path for login pupose
path('login/',views.login_user,name="login"),
#path for logout
path("logout/",views.logout_user,name='logout')

]