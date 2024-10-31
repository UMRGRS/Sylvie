from django_filters import rest_framework as filters

class MachineFilter(filters.FilterSet):
    identifier = filters.NumberFilter(field_name='identifier', lookup_expr='istartswith')
    machine = filters.CharFilter(field_name='machine', lookup_expr='icontains')
    area = filters.CharFilter(field_name='area', lookup_expr='icontains')