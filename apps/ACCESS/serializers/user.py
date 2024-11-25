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
            "email",
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
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
