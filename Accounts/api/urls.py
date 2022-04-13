from django.urls import path
from Accounts.api.views import (
    UserListView, UserDetail
)

app_name = 'Accounts'

urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'),
    path('list/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
