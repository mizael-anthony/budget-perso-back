from django.db.models import fields
from django_filters import filters
from django_filters.rest_framework import FilterSet
from .models import Action, Journal



class ActionFilterSet(FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='contains')

    max_cost= filters.NumberFilter(
            field_name='journals__cost',
            lookup_expr='lte')

    min_cost= filters.NumberFilter(
            field_name='journals__cost',
            lookup_expr='gte')

    max_date = filters.DateFilter(
            field_name='journals__date',
            lookup_expr='lte')

    min_date = filters.DateFilter(
            field_name='journals__date',
            lookup_expr='gte')


    class Meta:
        model = Action
        fields = ['name', 'category']


class JournalFilterSet(FilterSet):

    max_date = filters.DateFilter(
        field_name='date',
        lookup_expr='gte')

    min_date = filters.DateFilter(
        field_name='date',
        lookup_expr='lte')

    max_cost= filters.NumberFilter(
        field_name='cost',
        lookup_expr='gte')

    min_cost= filters.NumberFilter(
        field_name='cost',
        lookup_expr='lte')

    


    class Meta:
        model = Journal
        fields = ['action__category', 'date', 'cost']
