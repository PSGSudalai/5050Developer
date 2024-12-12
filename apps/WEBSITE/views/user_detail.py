from apps.ACCESS.models.user import User
from apps.BASE.base import AppAPIView
from apps.BASE.views import ListAPIViewSet
from apps.WEBSITE.serializers import UserDetailReadSerializer



class UserDetailAPIView(AppAPIView):
    def post(self, request):
        # Authenticate the user
        user = self.get_authenticated_user()
        if not user:
            return self.send_error_response({"error": "User not authenticated!"})

        # Extract data from the request
        name = request.data.get('name')
        dob = request.data.get('dob')
        phone = request.data.get('phone')
        college_name = request.data.get('college_name')
        address = request.data.get('address')

        # Validate that all required fields are provided
        if not all([name, dob, phone, college_name, address]):
            return self.send_error_response({"error": "All fields are required!"})

        # Update the user's information
        try:
            user.name = name
            user.dob = dob
            user.phone = phone
            user.college_name = college_name
            user.address = address
            user.save()

            # Prepare the response data
            data = {
                "name": user.name,
                "dob": user.dob,
                "phone": user.phone,
                "college": user.college_name,
                "address": user.address,
            }
            return self.send_response(data)
        except Exception as e:
            return self.send_error_response({"error": f"An error occurred: {str(e)}"})
    

class UserDetailListAPIView(ListAPIViewSet):
    serializer_class = UserDetailReadSerializer
    def get_queryset(self):
        user =self.get_authenticated_user()
        return User.objects.filter(user=user)


