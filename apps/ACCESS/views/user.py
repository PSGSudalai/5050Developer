from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from apps.ACCESS.models import User
from apps.ACCESS.serializers import UserSerializer
from apps.BASE.base import NonAuthenticatedAPIMixin
from apps.BASE.views import AppAPIView, AppCreateAPIView
from apps.BASE.config import API_RESPONSE_ACTION_CODES
from django.contrib.auth import logout as django_logout


class RegisterView(AppCreateAPIView, NonAuthenticatedAPIMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def perform_post_create(self, instance):
    #     token, _ = Token.objects.get_or_create(user=instance)
    #     return self.send_response()


class LoginView(AppAPIView, NonAuthenticatedAPIMixin):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            data = {"user": user.email, "id": user.id, "token": token.key}
            return self.send_response(data=data)
        return self.send_error_response(data={"detail": "Invalid Credentials"})


class LogoutView(AppAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = self.get_authenticated_user()
        print(user.full_name)
        token = Token.objects.get(user=user)
        django_logout(request)
        token.delete()
        return self.send_response()


class GetAuthUserDetails(AppAPIView):
    def get(self, request):
        user = self.get_authenticated_user()
        if user:
            data = {
                "uuid": user.uuid,
                "name": f"{user.full_name}",
                "email": user.email,
            }
            return self.send_response(data=data)
        return self.send_error_response()
