from django_filters import FilterSet
from farm_base.models import Farm

class FarmFilter(FilterSet):
    class Meta:
        model = Farm
        fields = {
            'name': ['icontains'],
            'municipality': ['exact'],
            'state': ['exact'],
            'owner__name': ['icontains'] # filter should be performed on the name of the related Owner model.
        }

    def owner_name_filter(queryset, name):
        '''
        Takes a queryset of farms and an owner name, 
        and returns a new queryset that includes only farms where the owner's name matches the provided value (case-insensitive).
        '''
        return queryset.filter(owner__name__icontains=name)