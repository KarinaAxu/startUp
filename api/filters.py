from django_filters import rest_framework as filters
from store.models import Restaurant, Menu

class RestaurantFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    address = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Restaurant
        fields = ['name', 'address']


class MenuFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    restaurant = filters.NumberFilter(field_name='restaurant__id')

    class Meta:
        model = Menu
        fields = ['name', 'restaurant']