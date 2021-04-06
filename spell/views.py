from django.shortcuts import render

# Create your views here.
def show_all_spells(request):
    return render(request, 'spell/show_all_spells.html')