from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from spell.models import Spell, Components, Spell_school
from spell.choices import spell_level_choices, casting_time_choices, duration_time_choices


# Create your views here.
def home(request):
    spells = Spell.objects.order_by('title')
    components = Components.objects.all()
    spell_school = Spell_school.objects.all()

    context = {
        'spells' : spells,
        'components' : components,
        'spell_schools' : spell_school,
        'spell_level_choices' : spell_level_choices,
        'casting_time_choices' : casting_time_choices, 
        'duration_time_choices' : duration_time_choices 
    }

    # Search from navbar only
    search_spell = request.GET.get('search')
    if search_spell:
        context['spells']= Spell.objects.filter(Q(title__icontains=search_spell))
        return render(request, 'user/home.html', context)

    # title
    if "title" in request.GET:
        title = request.GET['title']
        # Checking if title is empty
        if title:
            context['spells'] = spells.filter(title__icontains=title)

    # spell level
    if "spell_level" in request.GET:
        spell_level = request.GET['spell_level']
        if spell_level:
            context['spells'] = spells.filter(spell_level__icontains=spell_level)
    
    # casting time
    if "casting_time" in request.GET:
        casting_time = request.GET['casting_time']
        if casting_time:
            context['spells'] = spells.filter(casting_time__icontains=casting_time)
    
    # duration time
    if "duration_time" in request.GET:
        duration_time = request.GET['duration_time']
        if duration_time:
            context['spells'] = spells.filter(duration__icontains=duration_time)

    # spell school
    if "spell_school" in request.GET:
        spell_school = request.GET['spell_school']
        if spell_school:
            context['spells'] = spells.filter(spell_school__title=spell_school)
    # # verbal
    # if "verbal" in request.GET:
    #     verbal = request.GET['verbal']
    #     if verbal:
    #         context['spells'] = spells.filter(verbal__exact=True)
  
    return render(request, 'user/home.html', context)

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