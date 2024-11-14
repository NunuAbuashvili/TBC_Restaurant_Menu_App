from django_filters import rest_framework as filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from menu.models import MainCategory, SubCategory, MenuItem
from .serializers import (
    MainCategorySerializer,
    MiniMainCategorySerializer,
    BasicSubCategorySerializer,
    MiniSubCategorySerializer,
    AdvancedSubCategorySerializer,
    MenuItemSerializer
)
from .filters import SubCategoryFilter
from .permissions import IsRestaurantOwnerOrReadOnly


class MainCategoryViewSet(ListModelMixin,
                          CreateModelMixin,
                          GenericViewSet):
    """
    Viewset for managing main menu categories.

    Supports:
    - List view with minimal information.
    - Creation of new categories (authenticated users only)
    """
    queryset = MainCategory.objects.prefetch_related('restaurant')
    serializer_class = MainCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        """
        Return appropriate serializer class based on the action.
        """
        if self.action == 'list':
            return MiniMainCategorySerializer
        return MainCategorySerializer

    def perform_create(self, serializer):
        """
        Only the owner can create a new category under the restaurant.
        """
        restaurants = serializer.validated_data['restaurant']
        restaurants_failed = []

        for restaurant in restaurants:
            if self.request.user == restaurant.owner:
                serializer.save()

            else:
                restaurants_failed.append(restaurant.name)

        if restaurants_failed:
            raise PermissionDenied(
                f'You don\'t have permission to create a new category under {', '.join(restaurants_failed)}.'
            )


class SubCategoryViewSet(ListModelMixin,
                         CreateModelMixin,
                         RetrieveModelMixin,
                         UpdateModelMixin,
                         GenericViewSet):
    """
    Viewset for managing menu subcategories.

    Supports:
    - Filtered list view with minimal information.
    - Detailed view including related menu items.
    - Creation of new subcategories (authenticated users only)
    - Updates to existing subcategories (authenticated users only)

    Includes filtering by main category or menu item's name.
    """
    queryset = (SubCategory.objects
                .select_related('main_category')
                .prefetch_related('menu_items',
                                  'menu_items__ingredients',
                                  'main_category__restaurant'))
    serializer_class = BasicSubCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsRestaurantOwnerOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SubCategoryFilter

    def get_queryset(self):
        """
        Optimize the queryset for owner checks by prefetching restaurant owners.
        """
        queryset = super().get_queryset()
        if self.action in ['retrieve', 'update']:
            queryset = queryset.prefetch_related('main_category__restaurant__owner')
        return queryset

    def get_serializer_class(self):
        """
        Return appropriate serializer class based on the action.
        """
        if self.action == 'list':
            return MiniSubCategorySerializer
        elif self.action == 'retrieve':
            return AdvancedSubCategorySerializer
        return BasicSubCategorySerializer

    def perform_create(self, serializer):
        """
        Only the owner can create a new subcategory under the restaurant.
        """
        main_category = serializer.validated_data['main_category']
        restaurants = main_category.restaurant.all()
        failed = True

        for restaurant in restaurants:
            if restaurant.owner == self.request.user:
                serializer.save()
                failed = False

        if failed:
            raise PermissionDenied(
                f'You don\'t have permission to create a new subcategory under {main_category.name}.'
            )


class MenuItemViewSet(ListModelMixin,
                      CreateModelMixin,
                      UpdateModelMixin,
                      RetrieveModelMixin,
                      GenericViewSet):
    """
    Viewset for managing menu items.

    Supports:
    - Filtered list view
    - Detailed view of individual items
    - Creation of new menu items (authenticated users only)
    - Updates to existing menu items (authenticated users only)

    Includes filtering by subcategory and menu item's name (partial match).
    """
    queryset = (MenuItem.objects.select_related('restaurant', 'subcategory')
                .prefetch_related('ingredients'))
    serializer_class = MenuItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsRestaurantOwnerOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = {
        'subcategory': ['exact'],
        'name': ['icontains']
    }

    def get_queryset(self):
        """
        Optimize the queryset for owner checks by prefetching restaurant owners.
        """
        queryset = super().get_queryset()
        if self.action in ['retrieve', 'update']:
            queryset = queryset.prefetch_related('restaurant__owner')
        return queryset

    def perform_create(self, serializer):
        """
        Only the owner can create a new menu item under the restaurant.
        Also, subcategory must belong to the restaurant.
        """
        restaurant = serializer.validated_data['restaurant']
        subcategory = serializer.validated_data['subcategory']
        permission_message = ''

        if restaurant.owner != self.request.user:
            permission_message = f'You don\'t have permission to create a new menu item under {restaurant.name}.'
            raise PermissionDenied(permission_message)
        if not restaurant in subcategory.main_category.restaurant.all():
            permission_message = 'The restaurant you have chosen does not have this subcategory.'
            raise PermissionDenied(permission_message)

        serializer.save()
