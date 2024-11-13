from rest_framework import serializers

from menu.models import MainCategory, SubCategory, MenuItem, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)


class MenuItemSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = '__all__'


class MiniMenuItemSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = ('name', 'ingredients', 'image')


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = '__all__'


class BasicSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class MiniSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'image')


class AdvancedSubCategorySerializer(serializers.ModelSerializer):
    menu_items = MiniMenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ('name', 'menu_items')
