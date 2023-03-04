from django_filters import FilterSet, CharFilter
from farm_base.models import Farm

class FarmFilter(FilterSet):
    #  * The owner's name
    # * The owner's document number/identification
    # * The farm's name
    # * Municipality 
    # * State 
    # * The ID of the farm.
    # 
    owner__name = CharFilter(field_name='owner__name', lookup_expr='icontains')
    owner__document_number = CharFilter(field_name='owner__document_number', lookup_expr='exact')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    municipality = CharFilter(field_name='municipality', lookup_expr='exact')
    state = CharFilter(field_name='state', lookup_expr='exact')
    farm_id = CharFilter(field_name='id', lookup_expr='exact') # new filter for Farm ID

    class Meta:
        model = Farm
        fields = {
            'owner__name': ['icontains'], # filter should be performed on the name of the related Owner model.
            'owner__document_number': ['exact'],
            'name': ['icontains'],
            'municipality': ['exact'],
            'state': ['exact'],
            'id': ['exact']
        }