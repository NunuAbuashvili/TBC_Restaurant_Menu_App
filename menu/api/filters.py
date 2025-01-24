from django_filters import rest_framework as filters
from menu.models import SubCategory


class SubCategoryFilter(filters.FilterSet):
    """
    Filterset for Subcategory model providing various filtering options.

    Allows filtering subcategories by:
    - Main category
    - Menu item name (partial match)
    """
    menu_item_name = filters.CharFilter(
        field_name='menu_items__name',
        lookup_expr='icontains',
        label="Search by the menu item's name (contains)"
    )

    class Meta:
        model = SubCategory
        fields = ('main_category', 'menu_item_name')
