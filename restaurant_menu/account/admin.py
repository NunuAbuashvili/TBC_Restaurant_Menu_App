from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin configuration for CustomUser model.
    """
    list_display = ('username', 'email')
    search_fields = ('username',)
    search_help_text = _('Search by username')

    fieldsets = (
        (_('Account Information'), {
            'fields': ('username', 'password', 'is_active')
        }),
        (_('Personal Details'), {
            'fields': ('first_name', 'last_name', 'date_of_birth')
        }),
        (_('Contact Information'), {
            'fields': ('phone_number', 'email')
        }),
        (_('Permissions'), {
            'fields': ('groups', 'user_permissions', 'is_staff', 'is_superuser'),
            'classes': ('collapse',),
        }),
    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
