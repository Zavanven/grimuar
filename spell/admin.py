from django.contrib import admin
from .models import Spell_school, Spell, Components

# Register your models here.
class Spell_schoolAdmin(admin.ModelAdmin):
    list_display = ('title', )
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image_preview:
            return obj.image_preview
        return  
         
    image_preview.short_description = 'Logo obraz'
    image_preview.allow_tags = True

class SpellAdmin(admin.ModelAdmin):
    list_display = ('title', 'spell_level',)

admin.site.register(Spell_school, Spell_schoolAdmin)
admin.site.register(Spell, SpellAdmin)
admin.site.register(Components)