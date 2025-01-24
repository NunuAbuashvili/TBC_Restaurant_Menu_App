from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.api.urls', namespace='account')),
    path('restaurant/', include('restaurant.api.urls', namespace='restaurant')),
    path('menu/', include('menu.api.urls', namespace='menu')),
] + debug_toolbar_urls()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Restaurant Menu App'
admin.site.index_title = 'Restaurant Menu'