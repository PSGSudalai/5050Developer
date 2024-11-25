from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import EventWebListViewSet

API_URL_PREFIX = "api/"


router = SimpleRouter()
router.register("all/events", EventWebListViewSet)


urlpatterns = [
] + router.urls
