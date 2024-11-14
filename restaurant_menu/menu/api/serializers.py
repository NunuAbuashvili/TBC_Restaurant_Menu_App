from rest_framework import serializers
from menu.models import MainCategory, SubCategory, MenuItem, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """ Serializer for menu item ingredients. """
    class Meta:
        model = Ingredient
        fields = ('name',)


class MenuItemSerializer(serializers.ModelSerializer):
    """
    Menu item serializer for list views.

    Includes all menu item fields and related ingredients.
    """
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = '__all__'


class MiniMenuItemSerializer(serializers.ModelSerializer):
    """
    Simplified menu item serializer for subcategories' detailed views.

    Includes basic information and ingredient names as strings.
    """
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = ('name', 'ingredients', 'image')


class MainCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for detailed main category information.

    Used for creation, detailed views and update operation.
    """
    class Meta:
        model = MainCategory
        fields = '__all__'


class MiniMainCategorySerializer(serializers.ModelSerializer):
    """ Simplified main category serializer for list views. """
    class Meta:
        model = MainCategory
        fields = ('id', 'name')


class BasicSubCategorySerializer(serializers.ModelSerializer):
    """
    Basic serializer for subcategory information.

    Used for creation and update operations.
    """
    class Meta:
        model = SubCategory
        fields = '__all__'


class MiniSubCategorySerializer(serializers.ModelSerializer):
    """ Simplified subcategory serializer for list views. """
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'image')


class AdvancedSubCategorySerializer(serializers.ModelSerializer):
    """
    Subcategory serializer including related menu items.

    Used for detailed views of subcategories.
    """
    menu_items = MiniMenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ('name', 'menu_items')
