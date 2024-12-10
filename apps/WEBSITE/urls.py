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
] + router.urls
