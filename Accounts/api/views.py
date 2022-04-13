from rest_framework.generics import (
    ListAPIView, CreateAPIView, DestroyAPIView,
    RetrieveAPIView
)
from Accounts.models import User
from Accounts.api.serializers import UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
