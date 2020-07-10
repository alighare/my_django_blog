from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login
            user=form.save()  #we can equal user with form.save in line 12
                              #infact form.save get user informations
            login(request,user)
            return redirect('articles:list')
    else:
        form=UserCreationForm()
    return render(request,"user_accounts/signup.html",{"form":form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login user
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("articles:list")
    else:
        form=AuthenticationForm()
    return render(request,"user_accounts/login.html",{"form":form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("articles:list")
