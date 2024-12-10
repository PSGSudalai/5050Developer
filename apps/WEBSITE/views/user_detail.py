from apps.BASE.base import AppAPIView


class UserDetailAPIView(AppAPIView):
    def post(self,request):
        user = self.get_authenticated_user()
        print(user)
        if user:
            user.name = request.data.get('name')
            user.dob = request.data.get('dob')
            user.email = request.data.get('email')
            user.phone = request.data.get('phone')
            user.college = request.data.get('college_name')
            user.address = request.data.get('address')
            user.save()



            data ={
                "name":user.name,
                "dob":user.dob,
                "email":user.email,
                "phone":user.phone,
                "college":user.college,
                "address":user.addresss
            }
            return self.send_response(data=data)
        return self.send_error_response({"error":"Data Not Found!"})
    
