from rest_framework.serializers import ModelSerializer
from Workspace.models import Workspace
from Accounts.api.serializers import UserSerializer
from rest_framework import serializers


class MyWorkspaceListSerializer(ModelSerializer):
    member = UserSerializer(read_only=True)

    class Meta:
        model = Workspace
        fields = ('id', 'title', 'category_type', 'member')

    # def validate(self, attrs):
    #     if attrs['photo']:
    #         return attrs['photo'] == "The photo's url must be here"
    #     else:
    #         attrs['photo'] = None
    #     return attrs


class MyWorkspaceDetailSerializer(ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('id', 'title', 'category_type', 'website', 'description')


class MyWorkspaceCreateSerializer(ModelSerializer):
    member = UserSerializer(write_only=True)

    class Meta:
        model = Workspace
        fields = ('title', 'member','category_type', 'description')
