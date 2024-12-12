from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.BASE.views.generic import get_upload_api_view

from .views import(
        EventWebListViewSet,
        EventVideoAPIView,
        CertificateListAPIView,
        CreateOrderView,
        VerifyPaymentView,
        UserDetailAPIView,
        SubscriptionListAPIView,
        SubscriptionTableMeta,
        UserDetailListAPIView,

) 

app_name = "web"
API_URL_PREFIX = "api/"


router = SimpleRouter()
router.register("all/events", EventWebListViewSet)

router.register("certificate/list",CertificateListAPIView)






urlpatterns = [
    path("event/video/<uuid>/",EventVideoAPIView.as_view()),
    path("create-payment/", CreateOrderView.as_view(), name="create-order"),
    path("verify-payment/", VerifyPaymentView.as_view(), name="verify-payment"),
    path("user/detail/", UserDetailAPIView.as_view(), name="user-detail"),
    path("user/list/", UserDetailListAPIView.as_view({'get':'list'})),
    path("booking/table-meta/", SubscriptionTableMeta.as_view()),
    path("booking/event/",SubscriptionListAPIView.as_view({'get':'list'}),name="booking-event")
] + router.urls
