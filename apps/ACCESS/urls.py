from django.urls import path
from apps.ACCESS.views import LoginView, LogoutView, GetAuthUserDetails, RegisterView,ChangePassword,UserDetailAPIView
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "access"
API_URL_PREFIX = "api/"


router = SimpleRouter()



urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view({'get':'list'}), name="register"),
    path("register/table-meta/", RegisterView.as_view({'get':'get_meta_for_table'}), name="reghhjhhister"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/details/", GetAuthUserDetails.as_view(), name="login"),
    path("changepassword/", ChangePassword.as_view(), name="changepassword"),
    path("user/detail/",UserDetailAPIView.as_view()),
] + router.urls
