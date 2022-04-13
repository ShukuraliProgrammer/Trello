from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from Workspace.models import Workspace
from Board.models import Board
from Workspace.api.serializers import (
    MyWorkspaceDetailSerializer,
    MyWorkspaceListSerializer,
    MyWorkspaceCreateSerializer,
)


class MyWorkspaceListView(ListCreateAPIView):
    queryset = Workspace.objects.all()
    serializer_class = MyWorkspaceListSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.serializer_class
        elif self.request.method == "POST":
            return MyWorkspaceCreateSerializer
        else:
            return MyWorkspaceDetailSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(member=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)
        return serializer


class MyWorkspaceDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Workspace.objects.all()
    serializer_class = MyWorkspaceDetailSerializer


