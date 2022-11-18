from rest_framework import serializers

from users.models   import User

class UserModelSerializer(serializers.ModelSerializer):
    """유저 모델 serializer"""
    class Meta:
        model = User
        fields = "__all__"


class LoginSchema(serializers.Serializer):
    """로그인 파라미터 serializer"""
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=250)