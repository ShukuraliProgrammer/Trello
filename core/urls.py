from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('Accounts.api.urls')),
    path('api/workspace/', include('Workspace.api.urls')),
]
