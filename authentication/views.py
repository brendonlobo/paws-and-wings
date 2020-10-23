from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from post.views import show_post

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    if request.method  == 'POST':
        #check username and password exist or not
        user = auth.authenticate(username=request.POST['username'],password = request.POST['Password'])
        if user is not None:
            auth.login(request,user)
            return redirect(show_post)
        else:
            return render(request,'signin.html',{'error':'Invalid login Credentials'})
    else:
        return render(request,'signin.html')

def signup(request):
    if request.method == "POST":
        #create a user
        if request.POST['Password'] == request.POST['Passwordagain']:
            #Both password match
            #check user exist or not
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(request,'signup.html',{'error':"Username Already taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['Password'])
                auth.login(request,user)
                return redirect(show_post)
        else:
            return render(request,'signup.html',{'error':"Passwords Don't match"})

    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect(home)