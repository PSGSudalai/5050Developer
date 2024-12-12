from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
 
from apps.ADMIN.models import EventImage, DemoVideo
from apps.ADMIN.views import (
    EventCUDAPIViewSet,
    EventListAPIViewSet,
    EventHistoryListAPIView,
    RegisterEventListAPIView,
    CompleteEventListAPIView,
    LeaderBoardListAPIView,
    AdminDashboard,
    SubscriptionListAPIView,
    SubscriptionAPIView,
    SubscriptionTableMeta,
)
from apps.BASE.views import get_upload_api_view

app_name = "cms"
API_URL_PREFIX = "api/"


router = SimpleRouter()

router.register('event/list',EventListAPIViewSet,basename="event-list")
router.register('event/cud',EventCUDAPIViewSet,basename="event-cud")


router.register("event/history/list",EventHistoryListAPIView,basename="event-history-list")

router.register("register/event/list",RegisterEventListAPIView,basename="register-event-list")


router.register("complete/event/list",CompleteEventListAPIView,basename="complete-list")


router.register("leader/list",LeaderBoardListAPIView,basename="leaderlist")

urlpatterns = [
    path('event/image/',get_upload_api_view(meta_model=EventImage).as_view()),
    path('event/video/',get_upload_api_view(meta_model=DemoVideo).as_view()),
    path("dashboard/",AdminDashboard.as_view()),
    path("subscription/attendence/",SubscriptionAPIView.as_view()),
    path("subscription/table-meta/",SubscriptionTableMeta.as_view()),
    path("subscription/list/<uuid>/",SubscriptionListAPIView.as_view({'get':'list'}))

] + router.urls
