from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Spell, Components

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

    components = ModelMultipleChoiceField(
        queryset=Components.objects.all(),
        widget=CheckboxSelectMultiple
    )