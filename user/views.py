from django.shortcuts import render

# Create your views here.

def show_user_info(request):
    return render(request, 'user/show_user_info.html')

def signup_user(request):
    pass

def login_user(request):
    pass

def logout_user(request):
    pass