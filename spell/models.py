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