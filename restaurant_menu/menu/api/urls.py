from rest_framework import routers
from django.urls import path, include

from . import views


app_name = 'menu'
router = routers.DefaultRouter()
router.register(r'main-category-viewset', views.MainCategoryViewSet)
router.register(r'subcategory-viewset', views.SubCategoryViewSet)
router.register(r'menu-item-viewset', views.MenuItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
