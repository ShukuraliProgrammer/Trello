from rest_framework.serializers import ModelSerializer
from Accounts.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        if validated_data['email'] is None:
            user = ValueError
        else:
            user = User.objects.create(**validated_data)
        return user

