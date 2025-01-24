from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Restaurant(models.Model):
    """ Model representing a restaurant in the system. """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='restaurants'
    )
    name = models.CharField(_('restaurant name'), max_length=255)
    address = models.TextField(_('restaurant address'))
    phone_number = models.CharField(_('phone number'), max_length=13)
    image = models.ImageField(_('restaurant image'), upload_to='restaurant_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')
