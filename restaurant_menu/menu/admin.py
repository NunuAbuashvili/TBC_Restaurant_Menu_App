from django.contrib import admin
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _

from .models import MainCategory, SubCategory, MenuItem, Ingredient


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    search_help_text = _('Search by main category name.')
    ordering = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_category')
    list_select_related = ('main_category',)
    list_filter = ('main_category',)
    search_fields = ('name',)
    search_help_text = _('Search by subcategory name.')
    ordering = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'subcategory', 'restaurant')
    list_select_related = ('restaurant', 'subcategory')
    search_fields = ('name', 'restaurant')
    search_help_text = _('Search by menu item or restaurant name.')
    ordering = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    search_help_text = _('Search by ingredient name.')
