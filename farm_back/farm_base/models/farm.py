from django.contrib.gis.db import models
from django.utils.translation import gettext as _
from owner import Owner

class Farm(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255, null=False, blank=True)

    geometry = models.GeometryField(verbose_name=_("Geometry"), null=True, blank=True)

    area = models.FloatField(verbose_name=_("Area"), blank=True, null=True)

    centroid = models.PointField(verbose_name=_("Centroid"), blank=True, null=True)

    creation_date = models.DateTimeField(verbose_name=_("Creation date"), auto_now_add=True, editable=False)

    last_modification_date = models.DateTimeField(verbose_name=_("Last modification date"), auto_now=True)

    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)

    municipality = models.CharField(verbose_name=_("Municipality"), max_length=255, null=False, blank=True)
    
    state = models.CharField(verbose_name=_("State"), max_length=255, null=False, blank=True)

    # ForeignKey field owner ensures that one farm can have one and only one owner.    
    # related_name attribute allows to specify the name of the reverse relation from the Farm model to the Owner model.
    # Each Farm instance will have a related Owner instance accessible through the owner attribute.
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, related_name='farms', null=False, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['id']
        verbose_name = _('Farm')
        verbose_name_plural = _('Farms')
