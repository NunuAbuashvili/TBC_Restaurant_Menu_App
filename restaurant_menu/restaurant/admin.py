from django.contrib import admin
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _

from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    list_select_related = ('owner',)
    search_fields = ('name',)
    search_help_text = _('Search by restaurant name.')
