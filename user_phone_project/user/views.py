from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CustomUserCreationForm

#messages used to send message from server to client
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import logout,login


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.info(request,"Want an account to access Home")
        return redirect("login")
    else:
        user=request.user.username
        response=f"hello {user}"
        return HttpResponse(response)

def create_user(request):

    #check if the method is post when user tries to access the page it will be a get request
    if request.method == 'POST':
        #creating the instance of Form
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():

            #by using commit = False we can change the data before submitting
            #here we are manually setting the password 
            #here it will create the user object but will not save to db
            #you will have a reference to the object before saving
            user = form.save(commit=False)
            #set_password() hashes the password
            user.set_password(form.cleaned_data['password'])
            #now the new user object is saved to db
            user.save()
            
            return redirect('login')
        else:
            #if the creation fails the errors are send to the create.html using messaages
            messages.error(request,form.errors)
    form = CustomUserCreationForm()
    return render(request,"user/create.html",{"form":form})


def login_user(request):
    
    if request.method == 'POST':    
        password = request.POST['password']
        username_phone_email=request.POST['username_phone_email']
        
        #here the custom model backend will work first so if the user exists the user
        #variable will have the user instance else None
        user=authenticate(request,username=username_phone_email,password=password)
        
        if user is not None:
            #a new session created user is added in it
            login(request,user)
            #if user is not none redirect to home page
            return redirect('index')
        else:
            #if user has value None then raise the error User doesnot exist
            messages.error(request,"User doesn't exist")
            return redirect('login')

        
    return render(request,"user/login.html")
                

  
def logout_user(request):
    logout(request)
    return redirect('login')