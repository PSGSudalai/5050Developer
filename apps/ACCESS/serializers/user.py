from rest_framework import serializers
from apps.ACCESS.models import User
from rest_framework.authtoken.models import Token
from apps.BASE.serializers import read_serializer


# CustomUser Create Serializer
class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "student_id",
            "name",
            "phone",
            "address",
            "college_name",
            "dob",
            "email",
            "created",
            "password",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key

    def create(self, validated_data):
        email = validated_data.get("email")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": "A user with this email already exists."}
            )

        user = User(
            email=validated_data.get("email"),
            name=validated_data.get("name"),
            phone=validated_data.get("phone"),
            address=validated_data.get("address"),
            college_name=validated_data.get("college_name"),
            dob=validated_data.get("dob"),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
