from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'restaurant'
router = routers.DefaultRouter()
router.register(r'catalog', views.RestaurantViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
