from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from apps.ACCESS.models import User
from apps.ACCESS.serializers import UserSerializer
from apps.BASE.base import NonAuthenticatedAPIMixin
from apps.BASE.views import AppAPIView, AppCreateAPIView,CUDAPIViewSet,ListAPIViewSet
from apps.BASE.config import API_RESPONSE_ACTION_CODES
from django.contrib.auth import logout as django_logout
from rest_framework.generics import ListAPIView

class RegisterView(AppCreateAPIView, NonAuthenticatedAPIMixin,ListAPIViewSet,CUDAPIViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    all_table_columns ={
        "student_id":"ID",
        "name":"Name",
        "email":"Email",
        "phone":"Phone",
        "created":"Joining Date",
        "college_name":"College Name"

    }
    all_filters_name={}

    def get_meta_for_table(self, *args,**kwargs):
        data = {
            "column":self.all_table_columns,
            "filter":self.all_filters_name,
            "filter_data":{}
        }
        return self.send_response(data)


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
    

class ChangePassword(AppAPIView):
    def post(self, request, *args, **kwargs):
        user = self.get_authenticated_user()
        if not user or not user.is_authenticated:
            return self.send_error_response({"error": "User is not authenticated"})
        
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            return self.send_error_response({"detail": "Both old password and new password are required."})

        # Validate the old password
        if not user.check_password(old_password):
            return self.send_error_response({"detail": "Current password is incorrect."})

        if len(new_password) < 8:
            return self.send_error_response({"detail": "New password must be at least 8 characters long."})


        user.set_password(new_password)
        user.save()

        return self.send_response({"success": "Password has been changed successfully."})
    

# class UserTableMeta(ListAPIView, AppAPIView):
#     all_table_columns ={
#         "student_id":"ID",
#         "name":"Name",
#         "email":"Email",
#         "phone":"Phone",
#         "created":"Joining Date",
#         "college_name":"College Name"

#     }
#     all_filters_name={}

#     def get(self,*args,**kwargs):
#         data = {
#             "column":self.all_table_columns,
#             "filter":self.all_filters_name,
#             "filter_data":{}
#         }
#         return self.send_response(data)


class UserDetailAPIView(AppAPIView):
    def post(self, request, *args, **kwargs):
        # Get the authenticated user
        user = self.get_authenticated_user()
        if not user or not user.is_authenticated:
            return self.send_error_response({"error": "Non-authenticated user"})

        # Extract data from the request
        name = request.data.get("name")
        dob = request.data.get("dob")
        phone = request.data.get("phone")
        address = request.data.get("address")
        college_name = request.data.get("college_name")

        # Validate required fields
        missing_fields = []
        if not name:
            missing_fields.append("name")
        if not dob:
            missing_fields.append("dob")
        if not phone:
            missing_fields.append("phone")
        if not address:
            missing_fields.append("address")
        if not college_name:
            missing_fields.append("college_name")

        if missing_fields:
            return self.send_error_response(
                {"error": f"Missing required fields: {', '.join(missing_fields)}"}
            )

        # Save user details in the UserDetail model
        try:
            user_detail, created = User.objects.update_or_create(
                user=user,  # Link the details to the authenticated user
                defaults={
                    "name": name,
                    "dob": dob,
                    "phone": phone,
                    "address": address,
                    "college_name": college_name,
                },
            )

            # Prepare success message
            response_message = (
                "User details created successfully"
                if created
                else "User details updated successfully"
            )

            return self.send_response(
                {"message": response_message, "user_detail_id": user_detail.id}
            )

        except Exception as e:
            return self.send_error_response({"error": str(e)})
