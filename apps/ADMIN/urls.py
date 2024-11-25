from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.ADMIN.models import EventImage
from apps.ADMIN.views import EventCUDAPIViewSet, EventListAPIViewSet
from apps.BASE.views import get_upload_api_view

app_name = "cms"
API_URL_PREFIX = "api/"


router = SimpleRouter()

router.register('event/list',EventListAPIViewSet,basename="event-list")
router.register('event/cud',EventCUDAPIViewSet,basename="event-cud")


urlpatterns = [
    path('event/image/',get_upload_api_view(meta_model=EventImage).as_view())

] + router.urls
