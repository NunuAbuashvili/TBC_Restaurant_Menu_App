from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from restaurant.models import Restaurant
from .serializers import RestaurantSerializer, MiniRestaurantSerializer


class RestaurantViewSet(ListModelMixin,
                        CreateModelMixin,
                        GenericViewSet):
    """
    ViewSet for handling restaurant operations.

    Supports:
    - Listing restaurants (with minimal information)
    - Creating new restaurants (authenticated users only)
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        """
        Return appropriate serializer class based on the action.
        """
        if self.action == 'list':
            return MiniRestaurantSerializer
        return RestaurantSerializer

    def perform_create(self, serializer: RestaurantSerializer) -> None:
        """
        Set the owner of the restaurant to the current user when creating.
        """
        serializer.save(owner=self.request.user)
