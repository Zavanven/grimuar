from django.forms import ModelForm
from .models import Spell

class SpellForm(ModelForm):
    class Meta:
        model = Spell
        fields = [
            'title',
            'spell_school',
            'description',
            'higher_level',
            'spell_level',
            'casting_time',
            'duration',
            'components',
            'material_description',
            'concentration',
            'ritual',
        ]