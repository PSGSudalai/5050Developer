from django.urls import path
from apps.ACCESS.views import LoginView, LogoutView, GetAuthUserDetails, RegisterView
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "access"
API_URL_PREFIX = "api/"


router = SimpleRouter()

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/details/", GetAuthUserDetails.as_view(), name="login"),
] + router.urls
