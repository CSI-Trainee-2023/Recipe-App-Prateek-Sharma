from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Createrecipe
from .models import CreateRecipe
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    recipedata = CreateRecipe.objects.all()
    data = {'recipedata':recipedata}

    return render(request, 'home.html',data)

def SignupPage(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            messages.success(request, ('Your password and consent password are not same !!!'))
            return redirect('signup')
           
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
    
    return render(request, 'signup.html', {})

def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')

        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is Incorrect !!!")


    return render(request, 'login.html', {})

def LogoutPage(request):
    logout(request)
    return redirect('login')  

def CreatePage(request,id=0):
    if request.method == "GET":
        if id==0:
            form = Createrecipe()
        else:
            recipe=CreateRecipe.objects.get(pk=id)
            form = Createrecipe(instance=recipe)    
        return render(request, 'create.html', {'form':form})
    else: 
        if id==0:
            form = Createrecipe(request.POST)
        else:
            recipe=CreateRecipe.objects.get(pk=id)
            form = CreateRecipe(request.POST,instance=recipe)

        if form.is_valid():
            form.save()
        return redirect('home')
    

def Deleterecipe(request,id):
    recipe = CreateRecipe.objects.get(pk=id)
    recipe.delete()
    return redirect('home')
         