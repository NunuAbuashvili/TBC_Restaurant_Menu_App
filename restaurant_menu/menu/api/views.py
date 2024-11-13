from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from django_filters import rest_framework as filters

from menu.models import MainCategory, SubCategory, MenuItem
from .serializers import (
    MainCategorySerializer,
    BasicSubCategorySerializer,
    MiniSubCategorySerializer,
    AdvancedSubCategorySerializer,
    MenuItemSerializer
)


class MainCategoryViewSet(ListModelMixin,
                          CreateModelMixin,
                          RetrieveModelMixin,
                          UpdateModelMixin,
                          GenericViewSet):
    queryset = MainCategory.objects.prefetch_related('restaurant')
    serializer_class = MainCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SubCategoryFilter(filters.FilterSet):
    menu_item_name = filters.CharFilter(
        field_name='menu_items__name',
        lookup_expr='icontains',
        label="Search by the menu item's name (contains)"
    )

    class Meta:
        model = SubCategory
        fields = ('main_category', 'menu_item_name')


class SubCategoryViewSet(ListModelMixin,
                         CreateModelMixin,
                         RetrieveModelMixin,
                         UpdateModelMixin,
                         GenericViewSet):
    queryset = (SubCategory.objects
                .select_related('main_category')
                .prefetch_related('menu_items', 'menu_items__ingredients'))
    serializer_class = BasicSubCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SubCategoryFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return MiniSubCategorySerializer
        elif self.action == 'retrieve':
            return AdvancedSubCategorySerializer
        return BasicSubCategorySerializer


class MenuItemViewSet(ListModelMixin,
                      CreateModelMixin,
                      UpdateModelMixin,
                      RetrieveModelMixin,
                      GenericViewSet):
    queryset = (MenuItem.objects.select_related('restaurant', 'subcategory')
                .prefetch_related('ingredients'))
    serializer_class = MenuItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('subcategory',)
