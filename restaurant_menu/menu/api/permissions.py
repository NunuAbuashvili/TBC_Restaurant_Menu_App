from rest_framework import permissions
from menu.models import SubCategory, MenuItem

class IsRestaurantOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow restaurant owners to edit their subcategories.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, SubCategory):
            restaurants = obj.main_category.restaurant.all()
            return any(restaurant.owner == request.user for restaurant in restaurants)

        if isinstance(obj, MenuItem):
            return obj.restaurant.owner == request.user
