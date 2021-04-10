from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe
from django.core.files.images import get_image_dimensions

# Create your models here.
class Spell_school(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="spell/images")
    alt = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    @property
    def image_preview(self):

        if self.image:
            width, height = get_image_dimensions(self.image)
            return mark_safe('<img src="{}" width="{}" height="{}" class="admin-image-shop" />'.format(self.image.url, width, height))
        return ''

    class Meta:
        verbose_name = _("Spell school")
        verbose_name_plural = _("Spell schools")

# Komponenty
class Components(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Spell(models.Model):
    SPELL_LEVEL_CHOICES = [
        ('0', 'sztuczka'),
        ('1', '1. krąg'),
        ('2', '2. krąg'),
        ('3', '3. krąg'),
        ('4', '4. krąg'),
        ('5', '5. krąg'),
        ('6', '6. krąg'),
        ('7', '7. krąg'),
        ('8', '8. krąg'),
        ('9', '9. krąg'),
    ]

    ONE_ACTION = 1
    ONE_BONUS_ACTION = 2
    ONE_REACTION = 3
    ONE_MINUTE = 4
    TEN_MINUTES = 5
    ONE_HOUR = 6
    EIGHT_HOURS = 7
    TWELVE_HOURS = 8
    TWENTY_FOUR_HOURS = 9
    INSTANTANEOUS = 10
    UNTIL_DISPELED = 11
    ONE_ROUND = 12
    ONE_DAY = 13
    SEVEN_DAYS = 14
    TEN_DAYS = 15
    THIRTY_DAYS = 16
    SPECIAL = 17
    
    
    DURATION_TIME_CHOICES = [
        (INSTANTANEOUS, 'natychmiastowy'),
        (ONE_ROUND, '1 runda'),
        (ONE_MINUTE, '1 minuta'),
        (TEN_MINUTES, '10 minut'),
        (ONE_HOUR, '1 godzina'),
        (EIGHT_HOURS, '8 godzin'),
        (TWENTY_FOUR_HOURS, '24 godziny'),
        (TEN_DAYS, '10 dni'),
        (THIRTY_DAYS, '30 dni'),
        (SPECIAL, 'specjalny'),
        (UNTIL_DISPELED, 'do rozproszenia'),
    ]

    CASTING_TIME_CHOICES = [
        (ONE_ACTION, '1 akcja'),
        (ONE_BONUS_ACTION, '1 akcja dodatkowa'),
        (ONE_REACTION, 'reakcja'),
        (ONE_MINUTE, '1 minuta'),
        (TEN_MINUTES, '10 minut'),
        (ONE_HOUR, '1 godzina'),
        (EIGHT_HOURS, '8 godzin'),
        (TWELVE_HOURS, '12 godzin'),
        (TWENTY_FOUR_HOURS, '24 godziny'),
    ]

    title = models.CharField(max_length=200)
    spell_school = models.ForeignKey(Spell_school, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    higher_level = models.TextField(blank=True)
    spell_level = models.CharField(max_length=1, choices=SPELL_LEVEL_CHOICES, default=0)
    casting_time = models.IntegerField(choices=CASTING_TIME_CHOICES, default=ONE_ACTION)
    duration = models.IntegerField(choices=DURATION_TIME_CHOICES, default=ONE_ACTION)
    distance = models.CharField(max_length=50, blank=True)
    material_description = models.CharField(max_length=200, blank=True)
    concentration = models.BooleanField(default=False, blank=True)
    ritual = models.BooleanField(default=False, blank=True)
    components = models.ManyToManyField(Components, blank=True)

    def __str__(self):
        return self.title

    def is_verbal(self):
        if self.components.filter(title="Werbalny").exists():
            return True
        return False

    def is_somatic(self):
        if self.components.filter(title="Somatyczny").exists():
            return True
        return False
    
    def is_material(self):
        if self.components.filter(title="Materialny").exists():
            return True
        return False
