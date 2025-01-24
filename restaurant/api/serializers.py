from rest_framework import serializers
from restaurant.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new Restaurant instances.
    """
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'phone_number', 'image')


class MiniRestaurantSerializer(serializers.ModelSerializer):
    """
    Simplified restaurant serializer for list views.
    """
    class Meta:
        model = Restaurant
        fields = ('id', 'name')
