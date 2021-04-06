from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'user/home.html')

def show_user_info(request):
    return render(request, 'user/show_user_info.html')

def signup_user(request):
    if request.method == "GET":
        return render(request, 'user/signup.html', {'form' : UserCreationForm()})
    else:
        # Check if password1 and password 2 are the same
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'user/signup.html', {'form' : UserCreationForm(), 'error' : 'Nazwa użytkownika jest już zajęta.'})
        else:
            return render(request, 'user/signup.html', {'form' : UserCreationForm(), 'error' : 'Hasła się od siebie różnią. Spróbuj ponownie.'})

def login_user(request):
    if request.method == "GET":
        return render(request, 'user/login.html', {'form' : AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'user/login.html', {'form' : AuthenticationForm(), 'error' : 'Nazwa użytkownika lub hasło się nie zgadzają.'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')