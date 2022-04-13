from django.urls import path
from Workspace.api.views import MyWorkspaceListView, MyWorkspaceDetailView

urlpatterns = [
    path('list', MyWorkspaceListView.as_view(), name='list-create'),
    path('list/<int:pk>/', MyWorkspaceDetailView.as_view(), name='detail'),
]
