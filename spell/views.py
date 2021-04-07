from django.shortcuts import render, redirect
from .forms import SpellForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def show_all_spells(request):
    return render(request, 'spell/show_all_spells.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Editor').exists())
def create_spell(request):
    if request.method == "GET":
        return render(request, 'spell/create_spell.html', {'form' : SpellForm()})
    else:
        try:
            form = SpellForm(request.POST)
            form.is_valid()
            form.save()
            return render(request, 'spell/create_spell.html', {'form' : SpellForm(), 'alert' : 'Zaklecie zostalo dodane poprawnie.'})
        except ValueError:
            return render(request, 'spell/create_spell.html', {'form' : SpellForm(), 'error' : form.errors })
        
