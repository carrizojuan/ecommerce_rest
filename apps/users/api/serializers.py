from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()

    def validate_name(self, name):
        pass

    def validate_email(self, email):
        pass

    def validate(self, data):
        return super().validate(data)
