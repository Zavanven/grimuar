from django.shortcuts import render, redirect
from .forms import SpellForm

# Create your views here.
def show_all_spells(request):
    return render(request, 'spell/show_all_spells.html')

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
            return render(request, 'spell/create_spell.html', {'form' : SpellForm(), 'error' : 'Błąd. Jedno lub więcej pól jest błędnych.'})
        
