from django.db import models
from django.utils.translation import gettext_lazy as _

from restaurant.models import Restaurant


class MainCategory(models.Model):
    name = models.CharField(_('main category name'), max_length=100, unique=True)
    restaurant = models.ManyToManyField(Restaurant, related_name='main_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Main Category')
        verbose_name_plural = _('Main Categories')


class SubCategory(models.Model):
    name = models.CharField(_('subcategory name'), max_length=100, unique=True)
    image = models.ImageField(_('subcategory image'), upload_to='subcategory_images/')
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(_('menu item name'), max_length=255)
    image = models.ImageField(_('menu item image'), upload_to='menu_images/')
    price = models.DecimalField(_('menu item price'), max_digits=5, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menu Items')


class Ingredient(models.Model):
    name = models.CharField(_('ingredient name'), max_length=255)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
