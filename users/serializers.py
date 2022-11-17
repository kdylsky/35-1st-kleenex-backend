from rest_framework import serializers
from users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class LoginSchema(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=250)